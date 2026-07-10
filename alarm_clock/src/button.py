from machine import Pin
import time

# GPIO configuration
BUTTON_PIN_1 = 21  # The ESP32 pin GPIO21 connected to the button
button1 = Pin(BUTTON_PIN_1, Pin.IN, Pin.PULL_UP)

BUTTON_PIN_2 = 19  # The ESP32 pin GPIO21 connected to the button
button2 = Pin(BUTTON_PIN_2, Pin.IN, Pin.PULL_UP)

BUTTON_PIN_3 = 18  # The ESP32 pin GPIO21 connected to the button
button3 = Pin(BUTTON_PIN_3, Pin.IN, Pin.PULL_UP)

def button_act(log):

    if len(log) >= 50:
        del log[:20]

    if all(x == 0 for x in log[-5:]) == True:
        return 1

def button_act_short(log):
    if len(log) >= 50:
        del log[:20]

    if log[-1] == 0:
        return 1

def button_one(log):
    mode1 = False
    mode2 = False
    mode3 = False

    # Read the state of the button
    button_state = button1.value()
    log.append(button_state)

    # Print the button's state
    print(f"Button1: button-state: {button_state}")
    print(f"Button1: button-log: {log}")

    result = button_act(log)
    #print(result)
    if result == 1:
        mode1 = True

    return mode1, mode2, mode3
    # Wait for half a second before reading the button again
    # time.sleep(1)

def button_two(log):
    mode1 = False
    mode2 = False
    mode3 = False

    # Read the state of the button
    button_state = button2.value()
    log.append(button_state)

    # Print the button's state
    # print(f"Button2: button-state: {button_state}")
    # print(f"Button2: button-log: {log}")

    result = button_act_short(log)
    #print(result)
    if result == 1:
        mode1 = True

    return mode1, mode2, mode3
    # Wait for half a second before reading the button again
    # time.sleep(1)

def button_three(log):
    mode1 = False
    mode2 = False
    mode3 = False
    # Read the state of the button
    button_state = button3.value()
    log.append(button_state)

    # Print the button's state
    # print(f"Button3: button-state: {button_state}")
    # print(f"Button3: button-log: {log}")

    result = button_act_short(log)
    #print(result)
    if result == 1:
        mode1 = True

    return mode1, mode2, mode3
    # Wait for half a second before reading the button again
    # time.sleep(1)



def button_one_alarm(log):
    mode1 = False

    # Read the state of the button
    button_state = button1.value()
    log.append(button_state)

    # Print the button's state
    print("########## Button 1 ###########")
    print(f"Button1: button-state: {button_state}")
    print(f"Button1: button-log: {log}")
    print("###############################")

    result = button_act_short(log)
    #print(result)
    if result == 1:
        mode1 = True

    return mode1
    # Wait for half a second before reading the button again
    # time.sleep(1)

def button_two_alarm(log):
    mode2 = False

    # Read the state of the button
    button_state = button2.value()
    log.append(button_state)

    # Print the button's state
    print("########## Button 2 ###########")
    print(f"Button2: button-state: {button_state}")
    print(f"Button2: button-log: {log}")
    print("###############################")

    result = button_act_short(log)
    #print(result)
    if result == 1:
        mode2 = True

    return mode2
    # Wait for half a second before reading the button again
    # time.sleep(1)

def button_three_alarm(log):
    mode3 = False

    # Read the state of the button
    button_state = button3.value()
    log.append(button_state)

    # Print the button's state
    print("########## Button 3 ###########")
    print(f"Button3: button-state: {button_state}")
    print(f"Button3: button-log: {log}")
    print("###############################")
    print("\n\n")

    result = button_act_short(log)
    #print(result)
    if result == 1:
        mode3 = True

    return mode3
    # Wait for half a second before reading the button again
    # time.sleep(1)