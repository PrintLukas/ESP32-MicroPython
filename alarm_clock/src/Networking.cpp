#include "Networking.h"

#include <WiFi.h>

bool connectWiFi(const char* ssid, const char* password, uint32_t timeoutMs) {
    if (WiFi.status() == WL_CONNECTED) {
        return true;
    }

    Serial.println("connecting to network...");
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);

    uint32_t start = millis();
    while (WiFi.status() != WL_CONNECTED) {
        delay(100);
        if (millis() - start >= timeoutMs) {
            Serial.println("network connection can't be established");
            return false;
        }
    }

    Serial.print("network config: ");
    Serial.println(WiFi.localIP());
    return true;
}
