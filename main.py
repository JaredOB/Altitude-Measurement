from time import sleep
from machine import Pin, I2C
#from os import sys
#import bmp085
#os.system("bmp085.py")
#from test.test1 import Test1

from bmp085 import BMP180



led_onboard = Pin("LED", Pin.OUT)
i2c = I2C(0, sda = Pin(0), scl = Pin(1), freq = 1000000)

led_onboard.value(0)


while True:
    
#Sensor Configuration
    bmp = BMP180(i2c)
    bmp.oversample = 2
    bmp.sealevel = 101325
    temp = bmp.temperature
    press = bmp.pressure
    altitude = bmp.altitude
    temp_f= (temp * (9/5) + 32)
    pressure = "{:.2f}".format(press)
    alti = "{:.2f}".format(altitude)
    print(altitude)



