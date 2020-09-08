def on_forever():
    input.set_accelerometer_range(AcceleratorRange.FOUR_G)
    if input.button_is_pressed(Button.A) and input.acceleration(Dimension.X) >= 700 or input.button_is_pressed(Button.A) and input.acceleration(Dimension.X) <= -700:
        basic.show_icon(IconNames.NO)
        basic.pause(20)
        basic.clear_screen()
        basic.pause(20)
    elif input.button_is_pressed(Button.A) and input.acceleration(Dimension.Y) >= 700 or input.button_is_pressed(Button.A) and input.acceleration(Dimension.Y) <= -700:
        basic.show_icon(IconNames.NO)
        basic.pause(20)
        basic.clear_screen()
        basic.pause(20)
    elif input.button_is_pressed(Button.A) and input.acceleration(Dimension.Z) >= 700 or input.button_is_pressed(Button.A) and input.acceleration(Dimension.Z) <= -700:
        basic.show_icon(IconNames.NO)
        basic.pause(20)
        basic.clear_screen()
        basic.pause(20)
    else:
        basic.clear_screen()
        pins.analog_write_pin(AnalogPin.P0, 1023)
basic.forever(on_forever)
