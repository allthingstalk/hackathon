#!/bin/sh
# launcher.sh
# navigate to home dir, then to this dir, execute the python script, then back home


sleep 1  # pause so the os can init the pins

whilte true; do
  cd /
  cd home/pi
  cd hackathon
  sudo python PiHouse.py
  #sudo python PiHouseLED.py
done
cd /
