import alarm
import matrix
import networking
import time
import machine
#machine.reset()
import button
import b1m1
import buzzer
import bmp

output = matrix.displayTempPress(0)
matrix.displayString(output)
time.sleep(10)
#alarm_buzzer.alarm_sound()

networking.do_connect()
alarm.sync_time(retries=5)

# static values
set_alarm = [17,12]

# Button-States
button_log_1 = []
button_log_2 = []
button_log_3 = []

while True:
    display_time = alarm.time_hm()
    matrix.displayString(display_time)
    time.sleep(1)

    # Button 1
    modes1 = button.button_one(button_log_1)
    if modes1[0] == True:
        print("MODE1")
    elif modes1[1] == True:
        print("MODE2")
    elif modes1[2] == True:
        print("MODE3")

    # Button 2 
    modes2 = button.button_one(button_log_2)
    if modes2[0] == True:
        print("MODE1")
    elif modes2[1] == True:
        print("MODE2")
    elif modes2[2] == True:
        print("MODE3")

    # Button 3
    modes3 = button.button_one(button_log_3)
    if modes3[0] == True:
        print("MODE1")
    elif modes3[1] == True:
        print("MODE2")
    elif modes3[2] == True:
        print("MODE3")

    #print(display_time)
    if alarm.set_alarm(set_alarm) == True:
        matrix.alarm()




