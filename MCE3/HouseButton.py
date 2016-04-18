#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Important: before running this demo, make certain that grovepi & ATT_IOT
# are in the same directory as this script, or installed so that they are globally accessible
import logging
logging.getLogger().setLevel(logging.INFO)

import grovepi                                     #provides pin support
import ATT_IOT as IOT   #provide cloud support
from time import sleep                             #pause the app

#set up the ATT internet of things platform
IOT.DeviceId = ""
IOT.ClientId = ""
IOT.ClientKey = ""

#define each sensor
sensorName = "Button"
sensorPin = 5

actuatorPin = 6

#set up the pins
grovepi.pinMode(sensorPin,"INPUT")
grovepi.pinMode(actuatorPin,"OUTPUT")

#callback: handles values sent from the cloudapp to the device
def on_message(id, value):
  print("unknown actuator: " + id)
IOT.on_message = on_message

#make certain that the device & it's features are defined in the cloudapp
IOT.connect()
IOT.addAsset(sensorPin, sensorName, "Push button", False, "boolean")
IOT.subscribe()    

IOT.send("false", sensorPin)

buttonVal = False;
sensorVal = False;
while True:
  try:
    sensorRead = grovepi.digitalRead(sensorPin)
    if sensorRead == 255:
      continue
    if sensorVal != sensorRead:
      sensorVal = sensorRead
      if sensorVal:
        buttonVal = not buttonVal
        if buttonVal:
          IOT.send("true", sensorPin)
          grovepi.digitalWrite(actuatorPin, 1)          
        else:
          IOT.send("false", sensorPin)
          grovepi.digitalWrite(actuatorPin, 0)
  except IOError:
    print "error reading sensor"
