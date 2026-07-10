from machine import Pin
from time import sleep

buzzer = Pin(33, Pin.OUT)
buzzer.value(0)  # ensure silent at start

def alarm_sound():
    for x in range(5):
        buzzer.value(1)
        sleep(3)
        buzzer.value(0)
        sleep(0.5)
    