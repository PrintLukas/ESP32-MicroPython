# alarm.py
import ntptime, time



def time_hm():
    ntptime.settime()
    UTC_OFFSET = 2 * 3600  # e.g. UTC+1 → 3600 seconds; UTC-5 → -5 * 3600
    local = time.localtime(time.time() + UTC_OFFSET)

    year, month, mday, hour, minute, second, weekday, yearday = local
    print("{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        year, month, mday, hour, minute, second))

    return f"{hour:02d}{minute:02d}"