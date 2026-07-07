#pragma once

#include "Max7219Matrix.h"

// Port of matrix.py: turns the low-level driver into "show HHMM" / "blink for alarm".
class DisplayMatrix {
public:
    explicit DisplayMatrix(Max7219Matrix& driver);

    void showTime(const char* fourDigits);
    void alarmBlink();

private:
    Max7219Matrix& _driver;
};
