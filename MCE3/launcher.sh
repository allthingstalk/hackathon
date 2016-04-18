#!/bin/sh
# launcher.sh
# navigate to home dir, then to this dir, execute the python script, then back home

LOGFILE=/home/pi/hackathon/MCE3/restart.log

writelog() {
  now='date'
  echo ="$now $*" >> $LOGFILE
}

sleep 1  # pause so the os can init the pins

writelog "Starting"
whilte true; do
  cd /
  cd home/pi
  cd hackathon/MCE3
  #sudo python HouseButton.py
  #sudo python HouseLED.py
  writelog "Exited with status $?"
  writelog "Restarting"
done
cd /
