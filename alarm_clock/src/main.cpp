#include <Arduino.h>
#include <SPI.h>

#include "AlarmLogic.h"
#include "ButtonHandler.h"
#include "Config.h"
#include "DisplayMatrix.h"
#include "Max7219Matrix.h"
#include "Networking.h"

Max7219Matrix matrixDriver(MATRIX_CS_PIN, MATRIX_NUM_MODULES);
DisplayMatrix display(matrixDriver);
ButtonHandler buttons(BUTTON1_PIN, BUTTON2_PIN, BUTTON3_PIN);

void setup() {
    Serial.begin(115200);
    delay(200);

    SPI.begin(MATRIX_SCK_PIN, /*miso=*/-1, MATRIX_MOSI_PIN, MATRIX_CS_PIN);
    matrixDriver.begin();
    buttons.begin();

    connectWiFi(WIFI_SSID, WIFI_PASSWORD, 5UL * 60UL * 1000UL);
    Serial.println("hello?");
    syncTime(5);
}

void loop() {
    char hm[5] = "----";
    getCurrentHm(hm, sizeof(hm));
    display.showTime(hm);
    delay(1000);

    ButtonModes modes = buttons.poll();
    if (modes.mode1) {
        Serial.println("MODE1");
    } else if (modes.mode2) {
        Serial.println("MODE2");
    } else if (modes.mode3) {
        Serial.println("MODE3");
    }

    if (checkAlarm(ALARM_HOUR, ALARM_MINUTE)) {
        display.alarmBlink();
    }
}
