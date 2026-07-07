#pragma once

#include <Arduino.h>
#include <vector>

struct ButtonModes {
    bool mode1 = false;
    bool mode2 = false;
    bool mode3 = false;
};

// Port of button.py. Only button1 actually drives a mode (button2/3 are
// wired but unused in the original logic too -- carried over as-is).
class ButtonHandler {
public:
    ButtonHandler(uint8_t pin1, uint8_t pin2, uint8_t pin3);

    void begin();
    ButtonModes poll();

private:
    uint8_t _pin1, _pin2, _pin3;
    std::vector<int> _log;
};
