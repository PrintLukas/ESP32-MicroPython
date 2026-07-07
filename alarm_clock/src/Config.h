#pragma once

#include <Arduino.h>

// Wokwi simulation: uses the virtual "Wokwi-GUEST" network (no password)
static const char* const WIFI_SSID = "Wokwi-GUEST";
static const char* const WIFI_PASSWORD = "";

static const uint8_t MATRIX_CS_PIN = 25;
static const uint8_t MATRIX_SCK_PIN = 26;
static const uint8_t MATRIX_MOSI_PIN = 27;
static const uint8_t MATRIX_NUM_MODULES = 4;

static const uint8_t BUTTON1_PIN = 21;
static const uint8_t BUTTON2_PIN = 19;
static const uint8_t BUTTON3_PIN = 18;

static const int ALARM_HOUR = 14;
static const int ALARM_MINUTE = 40;
