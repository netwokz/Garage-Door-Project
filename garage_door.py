__author__ = 'netwokz'

# Raspberry Pi Temperature Logger Stephen M Deane Jr 
# www.thepowerofpi.com 6/5/2015

import RPi.GPIO as io
import time

relayPin = 4

io.setmode(io.BCM)
io.setup(relayPin, io.OUT, initial=1)

def activateGarage():
    try:
        io.output(relayPin, 0)
        time.sleep(.75)
        io.output(relayPin, 1)
    except: # Catch *all* exceptions. ToDo: fix this.
        io.cleanup()
