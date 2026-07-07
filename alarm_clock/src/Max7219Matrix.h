#pragma once

#include <Arduino.h>

// Direct port of the hand-rolled max7219.py driver: same command bytes,
// same per-module write order, so behavior in the Wokwi virtual chip is unchanged.
class Max7219Matrix {
public:
    Max7219Matrix(uint8_t csPin, uint8_t numModules);

    void begin();
    void brightness(uint8_t value);
    void fill(uint8_t color);
    void setRow(uint8_t moduleIndex, uint8_t row, uint8_t bits);
    void show();

    uint8_t numModules() const { return _num; }

private:
    void writeAll(uint8_t command, uint8_t data);

    uint8_t _cs;
    uint8_t _num;
    uint8_t* _buffer; // row-major: _buffer[row * _num + module]
};
