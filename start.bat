@echo off
title Minecraft Server Status
set /p address="Minecraft server address: "
set /p port="Server port (leave empty to use default port): "
if not defined port set port="25565"
python ./mc_server_check.py -ip %address% --port %port%
pause
