MAINTAINER frenzoid@protonmail.com

# We are using ubuntu 18.04 and not latest cause who knows if it works with the future versions.
FROM ubuntu:18.04

# Envs of the system, MOTD: THE WELCOME MESSAGE, ADMINPASSWORD: THE ADMIN PASSWORD....
ENV MOTD=WelcomeMessage \
    ADMINPASSWORD=admin \
    MAXPLAYERS=10 \
    SEED=26879 \
    MAXCONNPERIP=4 
    UPDATE=false

RUN mkdir -p /CubeWorld/config
COPY LICENSE /CubeWorld/LICENSE
COPY start.sh /CubeWorld

# Switching to the workdir
WORKDIR /CubeWorld

# Downloading the server and some binaries and update the system.
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y curl \ 
    git \
    build-essential \
    libsqlite3-dev \
    libssl-dev libbz2-dev \
    libreadline-dev \
    wget \
    curl \
    zlib1g-dev \
    nano

RUN curl -L https://git.io/vFLZX | bash

# Copying files.
COPY config/base.py /CubeWorld/config/base.py
COPY data/ /CubeWorld/data

# Exposing CubeWorld Port.
EXPOSE 12345

CMD [ "sh", "start.sh" ]

# Config folder: /CubeWorld/config
