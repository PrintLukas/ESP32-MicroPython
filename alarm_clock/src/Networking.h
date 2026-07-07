#pragma once

#include <Arduino.h>

// Port of networking.py's do_connect(): blocks (printing progress) until
// connected or timeoutMs elapses. Returns true on success.
bool connectWiFi(const char* ssid, const char* password, uint32_t timeoutMs);
