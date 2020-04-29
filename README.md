# CubeWorld on Docker!!
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/4/44/Cubeworld_logo.png"></img>
<p >
CubeWorld cuwo server implementation for docker.

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
- UPDATE: By default false, if true, it'll execute the update.sh, once updated, it will start the server automatically.

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
In case you run into any issue, dont be a dingus and just tell me via steam acc: [SrFrenzoid](https://steamcommunity.com/profiles/76561198050154084/) or [MrFrenzoid](https://steamcommunity.com/id/MrFren/), OR send me a message at frenzoid@protonmail.com.

This image was made using the [cuwo](http://cuwo.org/#about) open server implementation, written in Python and C++, for Cube World.

GitHub for this build here: https://github.com/Frenzoid/cuwo

Github of cuwo here: https://github.com/matpow2/cuwo

[Heres a nice music to listen while installing the docker image.](https://www.youtube.com/watch?v=_5w8SJ3yVsc)

Best regards and have a cool day!
More info at: https://hub.docker.com/r/xenium/cubeworld/

Have a nice day!
