# CubeWorldDockerServer
![CUBEWORLD SERVER](https://upload.wikimedia.org/wikipedia/commons/4/44/Cubeworld_logo.png)

CubeWorld server for docker.
==================

* * *
HOW TO LAUNCH
---

Just create a container with the image and expose the port 12345 on the host to whatever port you want (12345 too recomended) and start it.

* * *
ENV VARS
----
- ADMINPASSWORD: A password for the admin. (By default its "admin" so make sure to change this).
- MOTD: The welcome message of the server.
- SEED: The seed of the map generator  (Default value: 26879).
- MAXPLAYERS: The value of the amount of users that can be on the server at the same time. (Default is 10)
- MAXCONNPERIP: The value of the maxmium amount of connections per ip. (Default is 4)
- UPDATE: By default false, executes the update.sh, once done, it will start the server automatically.

* * *
EDITING PERMISSIONS AND STUFF
---
If you want to edit the permissions (to have more than an admin rank, lets say, helpers, moderators and admins) you'll need to login via interactive tty, edit the files with ```nano```, the files are at  ```/XENIUM/CubeWorld```, save them, and reboot the docker container.

For more info  about  how to do this, i would recommend to check the [cuwo docs](https://github.com/matpow2/cuwo/wiki) and [official page](http://cuwo.org/).

* * *
COMMANDS AND ADMIN COMMANDS
---
- Here my boy: [command list](https://github.com/matpow2/cuwo/wiki/Commands)
- Quick one: to login as admin just type ```/login [YOUR ENV ADMINPASSWORD VALUE]```

* * *
EXTRA STUFF TO READ
---
In case you run into any issue, dont be a dingus and just tell me via steam acc: [MrFrenzoid](https://steamcommunity.com/profiles/76561198050154084/), or send me a message at frenzoid@protonmail.com.

This image was made using the [cuwo](http://cuwo.org/#about) open server implementation, written in Python and C++, for Cube World.

GitHub for this build here: https://github.com/Frenzoid/CubeWorldDockerServer
Github of cuwo here: https://github.com/matpow2/cuwo

[Heres a nice music to listen while installing the docker image.](https://www.youtube.com/watch?v=_5w8SJ3yVsc)

Best regards and have a cool day!
More info at: https://hub.docker.com/r/xenium/cubeworld/

Have a nice day!


![cuwo](http://mp2.dk/cuwo/logo.png)
[![Build Status](https://travis-ci.org/matpow2/cuwo.svg?branch=master)](https://travis-ci.org/matpow2/cuwo) [![Build status](https://ci.appveyor.com/api/projects/status/t1ik17xyn26b8rx7?svg=true)](https://ci.appveyor.com/project/matpow2/cuwo)
====

cuwo is an open server implementation for Cube World, written in Python and
C++. It currently has the best protocol coverage among all the server projects
out there, and has features like

* Cross-platform support (Linux, Windows, Mac OS X, FreeBSD, what have you)
* NPCs and mobs, just as in the regular server
* File/console logging
* MOTD message
* Scripting (see the minimal welcome.py example)
* Advanced configuration
* Ban system
* Commands (/kick, /say, /whereis, /setclock, /kill, /stun. etc.)
* Rights management (/login password)
* IRC bot
* PvP script
* DDoS prevention
* Lower CPU requirements than normal server
* Optimizations in C++
* Master server on http://cuwo.org
* Support for 40+ players
* ... and much more!

Note that cuwo only supports x86 and x86-64, so it will not work on ARM.

Running
=======

Windows
-------

See the
[quick-start guide](https://github.com/matpow2/cuwo/wiki/Quickstart) for a
quick way to get started.

Alternatively, you can also
[build from source](https://github.com/matpow2/cuwo/wiki/WindowsSource).

Source
------

Make sure you have Python >= 3.6, native compilers, and the following
dependencies installed:

* `cython`
* `pyrr`

If you want IRC bot support, you will also need the `irc3` package.

These packages can be installed with `pip install cython pyrr irc3`

To build cuwo, run `python setup.py build_ext --inplace`.

To run the server, run `python -m cuwo.server`.

For more information, see
[this guide](https://github.com/matpow2/cuwo/wiki/BuildSource).

Status
======

In terms of the protocol and features, the following has been implemented:
* Player join/leave
* Player movement and animations
* Magic/arrows/etc. relay
* Player hits on entities/other players
* Item pickup/drop
* Time management
* Terrain generator
* Interactive objects (doors, beds)
* Preliminary support for Mobs and NPCs

A lot is still to be implemented gameplay-wise. Most importantly, NPCs and mobs
have only recently been implemented, so expect some issues related to these.

Other features include
* MITM proxy (for reverse-engineering)
* Cube World/Qubicle model converter (tools/convertqmo.py)
* Map viewer (tools/mapviewer.py)

FAQ
===

* **Q.** I get `ImportError: No module named 'cuwo.entity'` when running cuwo.

* **A.** See the instructions for running/building cuwo.

* **Q.** How do I pronounce 'cuwo'?

* **A.** 'coo-woo' (no, not 'kew-woh')

* **Q.** I am not a programmer, and I can't reverse-engineer anything. How do
         I help?

* **A.** We need people who can create end-user documentation as well! Have a
         look around, and see if anything is missing on the wiki.

* **Q.** What is a MITM proxy?

* **A.** A MITM proxy sits between your client and server, and can manipulate
         and inject packets. It's not really useful to the normal user, so
         use the regular cuwo server instead.

Special thanks
==============

```
9th - help with RE
Andoryuuta - native RE
BLACKROCK - for help on passive packet
ChrisMiuchiz - native patches and RE
ColdMeekly - help with AMD 64bit troubleshooting
cs475x - website design
DRayX - encrypt.py and protocol RE
Endimmion - for his generous Pledgie donation
Favorlock - scripting and commands
Kainzo - testing
Kyle - master server JS
Lord_Nightmare - terraingen help and support with x86
MAT4DOR - cub model details
MazeXD - master server JS and design
Perl - protocol RE
Sarcen - help with protocol variables, scripting, anticheat
SLoW - scripting
Somer - help with some protocol variables
uwee - protocol variables
Xaymar - RE and character details
ZeZeene - web interface for master server
```
