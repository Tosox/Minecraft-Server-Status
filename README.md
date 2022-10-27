# Minecraft Server Status

[![Python](https://img.shields.io/badge/Language-Python-yellow.svg?style=flat)](https://en.wikipedia.org/wiki/Python_(programming_language)) 
[![Minecraft](https://img.shields.io/badge/Game-Minecraft-green.svg?style=flat)](https://www.minecraft.net/en-us) 
[![Code size](https://img.shields.io/github/languages/code-size/TosoxDev/Minecraft-Server-Status?style=flat)](https://github.com/TosoxDev/Minecraft-Server-Status)
[![Lines of code](https://tokei.rs/b1/github/TosoxDev/Minecraft-Server-Status)](https://github.com/TosoxDev/Minecraft-Server-Status)

**A simple server status checker for minecraft written in python**

## Usage

```cmd
# Example
> python status_check.py -ip mc.hypixel.net --port 25565
``` 

| Argument          | Description                                  | Notes                        |
|-------------------|----------------------------------------------|------------------------------|
| -ip               | Server address                               |                              |
| --port            | Server address port                          | optional - Defaults to 25565 |

## Example results

```bash
# Successful
> python status_check.py -ip mc.hypixel.net
The server is up and running
```

```bash
# No server found
> python status_check.py -ip someserver.com
The server is offline or doesn´t exist
```

```bash
# The server is probably alive but not responding
> python status_check.py -ip anotherserver.net
Warning: the connection timed out
```

```bash
# No internet connection
> python status_check.py -ip mc.hypixel.net
Error: check your internet connection and try again
```

```bash
# Something went wrong when testing the connection
> python status_check.py -ip mc.hypixel.net
Error: couldn´t ping the server. Return code: XY
```

```bash
# Wrong syntax
> python status_check.py -address mc.hypixel.net -port
Error: please use the correct syntax: python status_check.py -ip <address> [OPTIONAL: --port <port>]
```
