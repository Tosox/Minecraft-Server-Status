# Minecraft Server Status

[![](https://img.shields.io/badge/Language-Python-yellow.svg?style=flat)](https://en.wikipedia.org/wiki/Python_(programming_language)) 
[![](https://img.shields.io/badge/Game-Minecraft-green.svg?style=flat)](https://www.minecraft.net/en-us) 
[![](https://img.shields.io/github/languages/code-size/TosoxDev/Minecraft-Server-Status?color=blue&label=Code%20size&style=flat)](https://github.com/TosoxDev/Minecraft-Server-Status)
[![](https://img.shields.io/tokei/lines/github/TosoxDev/Minecraft-Server-Status?color=red&label=Total%20lines&style=flat)](https://github.com/TosoxDev/Minecraft-Server-Status)
[![](https://img.shields.io/github/downloads/TosoxDev/Minecraft-Server-Status/total?color=green&label=Downloads&style=flat)](https://github.com/TosoxDev/Minecraft-Server-Status/releases)

**A simple server status checker for minecraft written in python**

## Usage

```cmd
# Example
> python mc_server_check.py -ip mc.hypixel.net --port 25565
``` 

| Arguments         | Description                                  | Notes                        |
|-------------------|----------------------------------------------|------------------------------|
| -ip               | Server address                               |                              |
| --port            | Server address port                          | optional - Defaults to 25565 |

## Example results

```bash
# Successful
> python mc_server_check.py -ip mc.hypixel.net
The server is up and running
```

```bash
# No server found
> python mc_server_check.py -ip someserver.com
The server is offline or doesn´t exist
```

```bash
# The server is probably alive but not responding
> python mc_server_check.py -ip anotherserver.net
Warning: the connection timed out
```

```bash
# No internet connection
> python mc_server_check.py -ip mc.hypixel.net
Error: check your internet connection and try again
```

```bash
# Something went wrong when testing the connection
> python mc_server_check.py -ip mc.hypixel.net
Error: couldn´t ping the server. Return code: XY
```

```bash
# Wrong syntax
> python mc_server_check.py -address mc.hypixel.net -port
Error: please use the correct syntax: python mc_server_check.py -ip <address> [OPTIONAL: --port <port>]
```
