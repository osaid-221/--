input.onButtonPressed(Button.A, function () {
    myVar += 3
    basic.showNumber(myVar)
})
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function () {
    myVar += -2
    basic.showNumber(myVar)
})
let myVar = 0
basic.showIcon(IconNames.Heart)
