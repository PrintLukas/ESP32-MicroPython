#pragma once

#include <Arduino.h>

// Port of alarm.py. configTime() bakes in the UTC+2 offset (equivalent of
// the original's manual UTC_OFFSET arithmetic), so getLocalTime() already
// returns local time.
bool syncTime(int retries = 3);

// Fills out with "HHMM" (out must be at least 5 bytes). Returns false if the
// time isn't available yet.
bool getCurrentHm(char* out, size_t outSize);

// Returns true if it is currently alarmHour:alarmMinute.
bool checkAlarm(int alarmHour, int alarmMinute);
