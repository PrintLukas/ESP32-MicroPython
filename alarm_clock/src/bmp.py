from machine import Pin, I2C
import time
from bmp180 import BMP180

i2c = I2C(0, scl=Pin(14), sda=Pin(32), freq=100000)
print(i2c.scan())
bmp = BMP180(i2c)

def returningTempPress():
        print("Temperature: {:.1f} C".format(bmp.temperature))
        print("Pressure: {} Pa".format(bmp.pressure))
        return bmp.temperature, bmp.pressure