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
actuatorName = "LED"
actuatorPin = 6

#set up the pins
grovepi.pinMode(actuatorPin,"OUTPUT")

#callback: handles values sent from the cloudapp to the device
def on_message(id, value):
    if id.endswith(str(actuatorPin)) == True:
        value = value.lower()                        	#make certain that the value is in lower case, for 'True' vs 'true'
        if value == "true":
            grovepi.digitalWrite(actuatorPin, 1)
            IOT.send("true", actuatorPin)                #provide feedback to the cloud that the operation was succesful
        elif value == "false":
            grovepi.digitalWrite(actuatorPin, 0)
            IOT.send("false", actuatorPin)               #provide feedback to the cloud that the operation was succesful
        else:
            print("unknown value: " + value)
    else:
        print("unknown actuator: " + id)
IOT.on_message = on_message

#make certain that the device & it's features are defined in the cloudapp
IOT.connect()
IOT.addAsset(actuatorPin, actuatorName, "Status LED", True, "boolean")
IOT.subscribe()

while True:
  sleep(3)