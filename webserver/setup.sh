#! /bin/bash

~/Projects/ShellScripts/microPython/burn.sh esp32 USB0 ~/Downloads/esp32-20180511-v1.9.4.bin

echo "Board booted"

echo "Run the following commands"
echo "ampy -p /dev/ttyUSB0 put pathTo[lib]"
echo "ampy -p /dev/ttyUSB0 put pathTo[wifiConnect.py]"
echo "ampy -p /dev/ttyUSB0 put pathTo[boot.py]"


echo "Reset the board manually"
