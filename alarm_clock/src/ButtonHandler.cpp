#include "ButtonHandler.h"

ButtonHandler::ButtonHandler(uint8_t pin1, uint8_t pin2, uint8_t pin3)
    : _pin1(pin1), _pin2(pin2), _pin3(pin3) {}

void ButtonHandler::begin() {
    pinMode(_pin1, INPUT_PULLUP);
    pinMode(_pin2, INPUT_PULLUP);
    pinMode(_pin3, INPUT_PULLUP);
}

ButtonModes ButtonHandler::poll() {
    ButtonModes modes;

    int state = digitalRead(_pin1);
    _log.push_back(state);
    Serial.printf("button-state: %d\n", state);

    if (_log.size() >= 50) {
        _log.erase(_log.begin(), _log.begin() + 20);
    }

    size_t start = _log.size() >= 5 ? _log.size() - 5 : 0;
    bool allLow = true;
    for (size_t i = start; i < _log.size(); i++) {
        if (_log[i] != 0) {
            allLow = false;
            break;
        }
    }
    if (allLow) {
        modes.mode1 = true;
    }

    return modes;
}
