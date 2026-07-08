# alarm.py
import ntptime, time

ntptime.host = "pool.ntp.org"
ntptime.timeout = 5   # default is only 1 second, which is often too short

def sync_time(retries=3):
    for attempt in range(retries):
        try:
            ntptime.settime()
            return True
        except OSError as e:
            print("NTP sync failed (attempt %d): %s" % (attempt + 1, e))
            time.sleep(2)
    return False

def update_time():
    UTC_OFFSET = 2 * 3600  # e.g. UTC+1 → 3600 seconds; UTC-5 → -5 * 3600
    local = time.localtime(time.time() + UTC_OFFSET)

    year, month, mday, hour, minute, second, weekday, yearday = local
    return year, month, mday, hour, minute, second, weekday, yearday
    #print("{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(year, month, mday, hour, minute, second))

def time_hm():
    year, month, mday, hour, minute, second, weekday, yearday = update_time()
    return f"{hour:02d}{minute:02d}"

def set_alarm(alarm):
    year, month, mday, hour, minute, second, weekday, yearday = update_time()
    alarm_hour, alarm_minute = alarm

    print(f"Time: {hour, minute}")
    print(f"Alarm: {alarm_hour, alarm_minute}")

    timer_minutes = ((alarm_hour * 60 + alarm_minute) - (hour * 60 + minute)) % 1440
    print(timer_minutes)

    if timer_minutes == 0:
        return True
    else:
        return timer_minutes




