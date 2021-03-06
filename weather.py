#!/usr/local/bin/python
import time 
import Adafruit_DHT 

def return_weather(pin):
    # Try to grab a sensor reading.  Use the read_retry method which 
    # will retry up to 15 times to get a sensor reading (waiting 2 
    # seconds between each retry).
    humidity, temp = Adafruit_DHT.read_retry(11, pin)
    # Note that sometimes you won't get a reading and the results will 
    # be null (because Linux can't guarantee the timing of calls to read 
    # the sensor). If this happens try again!
    if humidity is not None and temp is not None:
        Fahrenheit = (temp * 1.8) + 32
	F = "{:.0f}".format(Fahrenheit)
	H = "{:.0f}".format(humidity)
	print(Fahrenheit)
	print(humidity)
        weather = (F,H)
	return weather 

def main():
    get_weather() 

if __name__=='__main__':
    main()
