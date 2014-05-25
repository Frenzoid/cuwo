# Copyright (c) Mathias Kaerlev 2013-2014.
#
# This file is part of cuwo.
#
# cuwo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cuwo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cuwo.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from distutils.command import build_ext as _build_ext
import multiprocessing.pool
from distutils import log
from distutils.sysconfig import get_config_vars
from distutils import spawn
import subprocess


config_vars = get_config_vars()

# suppress warnings
IGNORE_FLAGS = ('-Wstrict-prototypes', '-mno-fused-madd')


def filter_flags(name):
    if name not in config_vars:
        return
    flags = config_vars[name].split()
    for flag in flags[:]:
        if flag in IGNORE_FLAGS:
            flags.remove(flag)
            continue
        if flag in ('-Os', '-O2', '-O1'):
            flags.append('-O3')
            flags.remove(flag)
            continue
    config_vars[name] = ' '.join(flags)

filter_flags('OPT')
filter_flags('CFLAGS')
filter_flags('CXXFLAGS')
filter_flags('ARCHFLAGS')


ext_modules = []

names = [
    'cuwo.bytes',
    'cuwo.entity'
]

includes = ['./cuwo', './terraingen/include']
lib_dir = './lib'

macros = []

if os.name == 'nt':
    macros += [('_CRT_SECURE_NO_WARNINGS', None)]

ext_modules.append(Extension('terraingen.pydasm', define_macros=macros,
                             sources=['./terraingen/pydasm/libdasm.c',
                                      './terraingen/pydasm/pydasm.pyx']))

tgen_module = Extension('cuwo.tgen', ['./cuwo/tgen.pyx'],
                        language='c++', include_dirs=includes,
                        library_dirs=[lib_dir], libraries=['tgen'])
ext_modules.append(tgen_module)

for name in names:
    ext_modules.append(Extension(name, ['./%s.pyx' % name.replace('.', '/')],
                                 language='c++', include_dirs=includes))


_spawn_nt = spawn._spawn_nt


def silent_spawn_nt(cmd, search_path=1, verbose=0, dry_run=0):
    executable = cmd[0]
    if search_path:
        # either we find one or it stays the same
        executable = spawn.find_executable(executable) or executable
    if dry_run:
        return
    # spawn for NT requires a full path to the .exe
    p = subprocess.Popen([executable] + cmd[1:], stdout=subprocess.PIPE)
    p.wait()
    rc = p.returncode
    if rc == 0:
        return
    # and this reflects the command running but failing
    raise spawn.DistutilsExecError(
        "command '%s' failed with exit status %d" % (cmd[0], rc))


class build_ext(_build_ext.build_ext):
    user_options = _build_ext.build_ext.user_options + [
        ('disable-tgen', None, 'disables the tgen extension')
    ]

    boolean_options = _build_ext.build_ext.boolean_options + [
        'disable-tgen'
    ]

    def initialize_options(self):
        super().initialize_options()
        self.disable_tgen = False

    def build_extensions(self):
        self.check_extensions_list(self.extensions)

        for ext in self.extensions:
            if ext.name == 'cuwo.tgen':
                if self.disable_tgen:
                    continue
                self.generate_tgen_sources(ext)
            self.build_extension(ext)

    def generate_tgen_sources(self, ext):
        if not self.force and os.path.isdir('./terraingen/gensrc'):
            return

        # get Server.exe if we don't have it already
        server_path = os.path.join(os.getcwd(), 'data', 'Server.exe')
        if os.path.isfile(server_path):
            with open(server_path, 'rb') as fp:
                server_data = fp.read()
        else:
            from urllib.request import urlopen
            print('Fetching tgen files...')
            server_data = urlopen('http://cuwo.org/get_executable.php').read()
            print('Done.')

        from terraingen.converter import convert
        print('Generating sources for tgen...')
        converter = convert(server_data)
        sources = [os.path.relpath(src) for src in converter.get_sources()]
        print('Generated %s source files.' % len(sources))

        print('Building static tgen library (this may take a while)')
        is_msvc = self.compiler.compiler_type == 'msvc'
        includes = converter.get_includes(is_msvc)
        extra_args = []
        if is_msvc:
            extra_args += ['/wd4102', '/EHsc', '/MP']
        else:
            extra_args += ['-w', '-fPIC', '-g0']

        class compile_state:
            index = 0

        # make a parallel build
        def compile_single(source):
            p = (compile_state.index * 100) // len(sources)
            p = '%02d' % p
            compile_state.index += 1
            sys.stdout.write('[%s%%] %s\n' % (p, os.path.basename(source)))
            sys.stdout.flush()
            return self.compiler.compile([source], output_dir=self.build_temp,
                                         macros=macros, include_dirs=includes,
                                         debug=self.debug,
                                         extra_postargs=extra_args)[0]

        spawn._spawn_nt = silent_spawn_nt
        old = log.set_threshold(log.WARN)
        # convert to list, imap is evaluated on-demand
        pool = multiprocessing.pool.ThreadPool(multiprocessing.cpu_count())
        objects = list(pool.imap(compile_single, sources))
        spawn._spawn_nt = _spawn_nt

        if os.name == 'nt':
            rsp_path = os.path.join(self.build_temp, 'link.rsp')
            fp = open(rsp_path, 'wb')
            data = ' '.join(objects).replace('\\', '/')
            fp.write(data.encode('utf-8'))
            fp.close()
            objects = ['@' + rsp_path]

        if is_msvc:
            objects += ['/NOLOGO']

        old_force = self.compiler.force
        self.compiler.force = True
        self.compiler.create_static_lib(objects, 'tgen',
                                        output_dir=os.path.relpath(lib_dir),
                                        debug=self.debug)
        self.compiler.force = old_force
        log.set_threshold(old)


setup(
    name='cuwo extensions',
    ext_modules=cythonize(ext_modules),
    cmdclass={"build_ext": build_ext}
)
