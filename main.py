__author__ = 'netwokz'

# Raspberry Pi Temperature Logger Stephen M Deane Jr 
# www.thepowerofpi.com 12/20/2015

import time 
import datetime 
import weather
import garage_door as garageDoor
import RPi.GPIO as io
from oled.device import ssd1306, sh1106
from oled.render import canvas
from PIL import ImageDraw, ImageFont

switchPin = 12
tempPin = 23
btnPin = 21
relayPin = 4
count = 0
isGarageClosed = False

# String Templates
mTemp = "Temperature: "
mHum  = "Humidity: "
temperatureData = [0,0]

# Button Setup
io.setmode(io.BCM)
io.setwarnings(False)
io.setup(tempPin, io.IN)
io.setup(switchPin,io.IN, pull_up_down=io.PUD_UP)
io.setup(btnPin, io.IN, pull_up_down=io.PUD_UP)
io.setup(relayPin, io.OUT, initial=1)


mLastView = 0 # 0 = temp, 1 = Garage

def getTemperature():
    global temperatureData
    temperatureData = weather.return_weather(tempPin)

def temperature():
    return "Temperature: %s F" \
           % (temperatureData[0])

def humidity():

    return "Humidity: %s %%" \
           % (temperatureData[1])

def garage():
    g = "open"
    return "Garage: %s " \
           % (g)

#def activateGarage():
#    io.output(relayPin, 0)
#    time.sleep(.75)
#    io.output(relayPin, 1)

def stats(oled):
    font = ImageFont.truetype('font.ttf', 12)
    mClosed = "Closed"
    mOpen = "Open"
    garage = ""
    if isGarageClosed == True:
        garage = "Garage is Closed"
    else:
        garage = "Garage is Open"
    with canvas(oled) as draw:
        draw.text((0, 12), temperature(), font=font, fill=255)
        draw.text((0, 26), humidity(), font=font, fill=255)
        draw.text((0, 40), garage, font=font, fill=255)

def clearScreen(oled):
    font = ImageFont.truetype('font.ttf', 12)
    with canvas(oled) as draw:
        draw.rectangle((0,0,oled.width,oled.height),outline=0,fill=0)
        
def main():
    oled = sh1106(port=1, address=0x3C)
    stats(oled)

if __name__ == "__main__":
    main()

try:
    oled = sh1106(port=1, address=0x3C)
    getTemperature()
    while count < 1:
        garage = io.input(btnPin)
        if garage == False:
            print('Button Pressed')
            garageDoor.activateGarage()
        if io.input(switchPin):
            isGarageClosed = False
        else:
            isGarageClosed = True
        stats(oled)
        #count += 1
            
except KeyboardInterrupt:
    print("****user exit****")
finally:
    #io.output(relayPin, 1)
    io.cleanup()
    clearScreen(oled)
