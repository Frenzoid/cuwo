FROM ubuntu:18.04
MAINTAINER frenzoid@protonmail.com

# Envs of the system, MOTD: THE WELCOME MESSAGE, ADMINPASSWORD: THE ADMIN PASSWORD....
ENV MOTD=WelcomeMessage \
    ADMINPASSWORD=admin \
    MAXPLAYERS=10 \
    SEED=26879 \
    MAXCONNPERIP=4 \
    UPDATE=false

RUN mkdir -p /CubeWorld/config
RUN echo "P3: $(python3 -V), P2: $(python -V)"
COPY LICENSE /CubeWorld/LICENSE

# Switching to the workdir
WORKDIR /CubeWorld

# Downloading the server and some binaries and update the system.
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y curl \ 
    git \
    python3-pip \
    python3-dev \
    build-essential \
    libsqlite3-dev \
    libssl-dev libbz2-dev \
    libreadline-dev \
    wget \
    curl \
    zlib1g-dev \
    nano
    
RUN ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip \
    && curl -L https://git.io/vFLZX | bash

# Copying files.
COPY config/base.py /CubeWorld/config/base.py
COPY data/ /CubeWorld/data
COPY start.sh /CubeWorld/start.sh


# Exposing CubeWorld Port.
EXPOSE 12345

CMD [ "sh", "start.sh" ]

# Config folder: /CubeWorld/config
