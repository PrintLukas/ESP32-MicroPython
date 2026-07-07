#include "DisplayMatrix.h"

#include <Arduino.h>

#include "Font8x8Digits.h"

DisplayMatrix::DisplayMatrix(Max7219Matrix& driver) : _driver(driver) {}

void DisplayMatrix::showTime(const char* fourDigits) {
    _driver.brightness(2); // crank it up -- begin() leaves this at a possibly-dim default
    _driver.fill(0);
    for (uint8_t i = 0; i < _driver.numModules() && fourDigits[i] != '\0'; i++) {
        char c = fourDigits[i];
        if (c >= '0' && c <= '9') {
            const uint8_t* glyph = kDigitFont[c - '0'];
            for (uint8_t row = 0; row < 8; row++) {
                _driver.setRow(i, row, glyph[row]);
            }
        }
    }
    _driver.show(); // nothing appears until you call this
}

void DisplayMatrix::alarmBlink() {
    _driver.brightness(15);
    for (int i = 0; i < 5; i++) {
        _driver.fill(0);
        _driver.show();
        delay(1000);
        _driver.fill(1);
        _driver.show();
        delay(1000);
    }
}
