import alarm
import matrix
import networking
import time

networking.do_connect()

while True:
    display_time = alarm.time_hm()
    matrix.test(display_time)
    time.sleep(1)
    #print(display_time)
