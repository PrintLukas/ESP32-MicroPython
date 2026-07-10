import alarm
import matrix
import networking
import time
import machine
#machine.reset()
import button
import b1
import buzzer
import bmp

#--------------Test-Zone---------------


#set_alarm = [6,0]
#set_alarm = matrix.set_alarm(set_alarm)


#---------------------------------------



# output = matrix.displayTempPress(0)
# matrix.displayString(output)
time.sleep(10)
#alarm_buzzer.alarm_sound()

networking.do_connect()
alarm.sync_time(retries=5)

# static values
set_alarm = [6,30]

 
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
        print("MODE1.1")
        set_alarm = matrix.set_alarm(set_alarm)
        print(set_alarm)
    elif modes1[1] == True:
        print("MODE1.2")
    elif modes1[2] == True:
        print("MODE1.3")

    # Button 2 
    modes2 = button.button_two(button_log_2)
    if modes2[0] == True:
        print("MODE2.1")
        output = matrix.displayTempPress(0)
        matrix.displayString(output)
    elif modes2[1] == True:
        print("MODE2.2")
    elif modes2[2] == True:
        print("MODE2.3")

    # Button 3
    modes3 = button.button_three(button_log_3)
    if modes3[0] == True:
        print("MODE3.1")
        output = matrix.displayTempPress(1)
        matrix.displayString(output)
    elif modes3[1] == True:
        print("MODE3.2")
    elif modes3[2] == True:
        print("MODE3.3")

    #print(display_time)
    if alarm.set_alarm(set_alarm) == True:
        matrix.alarm()




