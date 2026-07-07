#include "Max7219Matrix.h"

#include <SPI.h>
#include <string.h>

namespace {
constexpr uint8_t DIGIT0 = 1;
constexpr uint8_t DECODEMODE = 9;
constexpr uint8_t INTENSITY = 10;
constexpr uint8_t SCANLIMIT = 11;
constexpr uint8_t SHUTDOWN = 12;
constexpr uint8_t DISPLAYTEST = 15;

SPISettings matrixSpiSettings() {
    return SPISettings(10000000, MSBFIRST, SPI_MODE0);
}
} // namespace

Max7219Matrix::Max7219Matrix(uint8_t csPin, uint8_t numModules)
    : _cs(csPin), _num(numModules) {
    _buffer = new uint8_t[8 * _num];
}

void Max7219Matrix::begin() {
    pinMode(_cs, OUTPUT);
    digitalWrite(_cs, HIGH);
    fill(0);

    writeAll(SHUTDOWN, 0);
    writeAll(DISPLAYTEST, 0);
    writeAll(SCANLIMIT, 7);
    writeAll(DECODEMODE, 0);
    writeAll(SHUTDOWN, 1);
}

void Max7219Matrix::writeAll(uint8_t command, uint8_t data) {
    SPI.beginTransaction(matrixSpiSettings());
    digitalWrite(_cs, LOW);
    for (uint8_t m = 0; m < _num; m++) {
        SPI.transfer(command);
        SPI.transfer(data);
    }
    digitalWrite(_cs, HIGH);
    SPI.endTransaction();
}

void Max7219Matrix::brightness(uint8_t value) {
    if (value > 15) value = 15;
    writeAll(INTENSITY, value);
}

void Max7219Matrix::fill(uint8_t color) {
    memset(_buffer, color ? 0xFF : 0x00, 8 * _num);
}

void Max7219Matrix::setRow(uint8_t moduleIndex, uint8_t row, uint8_t bits) {
    _buffer[row * _num + moduleIndex] = bits;
}

void Max7219Matrix::show() {
    SPI.beginTransaction(matrixSpiSettings());
    for (uint8_t y = 0; y < 8; y++) {
        digitalWrite(_cs, LOW);
        for (uint8_t m = 0; m < _num; m++) {
            SPI.transfer(DIGIT0 + y);
            SPI.transfer(_buffer[y * _num + m]);
        }
        digitalWrite(_cs, HIGH);
    }
    SPI.endTransaction();
}
