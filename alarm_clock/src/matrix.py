# matrix.py

from machine import Pin, SPI
import max7219
import time

spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(26), mosi=Pin(27))
cs = Pin(25, Pin.OUT)
display = max7219.Matrix8x8(spi, cs, 4)

def test(txt):
    display.brightness(7)   # crank it up — init() leaves this at a possibly-dim default
    display.fill(0)
    display.text(txt, 0, 0, 1)
    display.show()                 # nothing appears until you call this
