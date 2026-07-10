# matrix.py
from machine import Pin, SPI, I2C
import max7219
import time
import buzzer
import bmp
import button

# Matrix-Panel-PIN-Definition
spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(26), mosi=Pin(27))
cs = Pin(25, Pin.OUT)
display = max7219.Matrix8x8(spi, cs, 4)

def displayString(txt):
    display.brightness(10)
    display.fill(0)
    display.text(txt, 0, 0, 1)
    display.show()

def set_alarm(alarm):
    display.brightness(15)
    # Button-States
    button_log_1 = []
    button_log_2 = []
    button_log_3 = []

    

    alarm_value = []
    alarm_hour = alarm[0]
    alarm_min = alarm[1]
    alarm_setting_status = True

    while alarm_setting_status == True:

        alarm_hour_str = str(alarm_hour)
        alarm_min_str = str(alarm_min)
        alarm_hour_str, alarm_min_str = oneNumberHandler(alarm_hour_str, alarm_min_str)
        str_alarm = alarm_hour_str+alarm_min_str

        display.text(str_alarm, 0, 0, 1)
        display.show()
        time.sleep(0.5)
        display.fill(0)
        display.show()
        time.sleep(0.5)

        # Button 1
        mode_set = button.button_one_alarm(button_log_1)
        if mode_set == True:
            # converting str to int
            alarm_hr_int = int(str_alarm[:2])
            alarm_mn_int = int(str_alarm[2:])            
            # store alarm an leave the function
            alarm_value.append(alarm_hr_int)
            alarm_value.append(alarm_mn_int)

            print(f'alarm set to {alarm_value}')
            alarm_setting_status = False
            

        # Button 2 
        mode_increase_hour = button.button_two_alarm(button_log_2)
        if mode_increase_hour == True:
            alarm_hour = (alarm_hour + 1) % 24
            print(mode_increase_hour)
            

        # Button 3
        mode_increase_minute = button.button_three_alarm(button_log_3)
        if mode_increase_minute == True:
            alarm_min = (alarm_min + 5) % 60
            print(mode_increase_minute)
        
    return alarm_value
            


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

def oneNumberHandler(hour, minute):
    if isinstance(hour, str) and isinstance(minute, str):
        if len(hour) == 1:
            hour = "0" + hour
        if len(minute) == 1:
            minute = "0" + minute
    return hour, minute
