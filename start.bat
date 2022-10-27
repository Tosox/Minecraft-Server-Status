@echo off
title Minecraft Server Status
set /p address="Minecraft server address: "
set /p port="Server port (leave empty to use default port): "
if "%port%"==[] set port="25565"
python ./status_check.py -ip %address% --port %port%
pause
