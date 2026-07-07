#include "AlarmLogic.h"

#include <time.h>

namespace {
constexpr long kGmtOffsetSec = 2 * 3600; // UTC+2, matches original UTC_OFFSET
constexpr int kDaylightOffsetSec = 0;
constexpr char kNtpServer[] = "pool.ntp.org";
} // namespace

bool syncTime(int retries) {
    configTime(kGmtOffsetSec, kDaylightOffsetSec, kNtpServer);

    struct tm timeinfo;
    for (int attempt = 0; attempt < retries; attempt++) {
        if (getLocalTime(&timeinfo, 5000)) {
            return true;
        }
        Serial.printf("NTP sync failed (attempt %d)\n", attempt + 1);
        delay(2000);
    }
    return false;
}

bool getCurrentHm(char* out, size_t outSize) {
    struct tm timeinfo;
    if (!getLocalTime(&timeinfo, 100)) {
        return false;
    }
    snprintf(out, outSize, "%02d%02d", timeinfo.tm_hour, timeinfo.tm_min);
    return true;
}

bool checkAlarm(int alarmHour, int alarmMinute) {
    struct tm timeinfo;
    if (!getLocalTime(&timeinfo, 100)) {
        return false;
    }

    int hour = timeinfo.tm_hour;
    int minute = timeinfo.tm_min;
    int timerMinutes = ((alarmHour * 60 + alarmMinute) - (hour * 60 + minute) + 1440) % 1440;

    Serial.printf("Time: %d:%d\n", hour, minute);
    Serial.printf("Alarm: %d:%d\n", alarmHour, alarmMinute);
    Serial.printf("Minutes to alarm: %d\n", timerMinutes);

    return timerMinutes == 0;
}
