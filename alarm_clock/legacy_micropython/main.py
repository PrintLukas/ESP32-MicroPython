import alarm
import matrix
import networking
import time
import machine
#machine.reset()
import button
import b1m1

networking.do_connect()
print("hello?")
alarm.sync_time(retries=5)
# static values
set_alarm = [14, 40]
button_log = []

while True:
    display_time = alarm.time_hm()
    #display_time = "cafe"
    matrix.test(display_time)
    time.sleep(1)

    # mode1, mode2, mode3
    modes = button.button_one(button_log)
    if modes[0] == True:
        print("MODE1")
    elif modes[1] == True:
        print("MODE2")
    elif modes[2] == True:
        print("MODE3")

    #print(display_time)
    if alarm.set_alarm(set_alarm) == True:
        matrix.alarm()




