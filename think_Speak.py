import sys
import urllib
import time
import dht11
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from urllib.request import urlopen
# Enter Your API key here
myAPI = ''
# URL where we will send the data, Don't change it
BASE_URL = "https://api.thingspeak.com/update?api_key={}".format(myAPI)
instance = dht11.DHT11(pin=21)
while True:
   
        
    if __name__ == "__main__":
        try:
            while True:
          
                time.sleep(1)
                result = instance.read()
        
                temp = result.temperature
                humi = result.humidity            

                #humi, temp = DHT11_data()
                
                humi = '%.2f' % humi 
                temp = '%.2f' % temp                      
                        
                # Sending the data to thingspeak
                conn = urlopen(BASE_URL + '&field1=%s&field2=%s' % (humi,temp))
            
                conn.read()
                print("Temperature=",temp)
                #for printing data on our screen
                print("Humidity=",humi)
                # Closing the connection
                conn.close()
                
                time.sleep(10)

        except KeyboardInterrupt:
            GPIO.cleanup()


