def on_button_pressed_a():
    global myVar
    myVar += 3
    basic.show_number(myVar)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global myVar
    myVar += -2
    basic.show_number(myVar)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

myVar = 0
basic.show_icon(IconNames.HEART)