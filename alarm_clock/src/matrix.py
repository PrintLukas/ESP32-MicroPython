# matrix.py
from machine import Pin, SPI, I2C
import max7219
import time
import buzzer
import bmp

# Matrix-Panel-PIN-Definition
spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(26), mosi=Pin(27))
cs = Pin(25, Pin.OUT)
display = max7219.Matrix8x8(spi, cs, 4)

def displayString(txt):
    display.brightness(10)
    display.fill(0)
    display.text(txt, 0, 0, 1)
    display.show()

def set_alarm():
    #displayed_time =
    pass

def alarm():
    display.brightness(15)
    i = 5
    while i > 0:
        display.fill(0)
        display.show()
        buzzer.alarm_sound()
        time.sleep(1)
        display.fill(1)
        display.show()
        time.sleep(1)
        i -= 1

def displayTempPress(tempOrPress):
    # if temperature should be displayed = 0
    # if pressure should be displayed = 1

    tempPress = bmp.returningTempPress()
    temp, press = tempPress
    temp = str(temp)
    press = str(press)

    # preparing the strings for matrix-display
    temp = temp
    press = press[:4]
    print(temp,press)

    if tempOrPress == 0: 
        dispTemp = temp
        print(dispTemp)
        for x in range (2):
            displayString(dispTemp)
            time.sleep(2)
            displayString(" Cel")
            time.sleep(2)
        return dispTemp

    elif tempOrPress == 1:
        dispPress = press
        for x in range (2):
            displayString(dispPress)
            time.sleep(2)
            displayString(" hPa")
            time.sleep(2)
        return dispPress

    