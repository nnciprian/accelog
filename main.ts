basic.forever(function () {
    input.setAccelerometerRange(AcceleratorRange.FourG)
    if (input.buttonIsPressed(Button.A) && input.acceleration(Dimension.X) >= 700 || input.buttonIsPressed(Button.A) && input.acceleration(Dimension.X) <= -700) {
        basic.showIcon(IconNames.No)
        basic.pause(20)
        basic.clearScreen()
        basic.pause(20)
    } else if (input.buttonIsPressed(Button.A) && input.acceleration(Dimension.Y) >= 700 || input.buttonIsPressed(Button.A) && input.acceleration(Dimension.Y) <= -700) {
        basic.showIcon(IconNames.No)
        basic.pause(20)
        basic.clearScreen()
        basic.pause(20)
    } else if (input.buttonIsPressed(Button.A) && input.acceleration(Dimension.Z) >= 700 || input.buttonIsPressed(Button.A) && input.acceleration(Dimension.Z) <= -700) {
        basic.showIcon(IconNames.No)
        basic.pause(20)
        basic.clearScreen()
        basic.pause(20)
    } else {
        basic.clearScreen()
    }
})
