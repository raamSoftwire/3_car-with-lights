def set_led_color(ledNumber: number, incoming_speed: number, threshold: number, colour: number):
    if incoming_speed > threshold:
        bitbot.set_pixel_color(ledNumber, colour)
    else:
        bitbot.set_pixel_color(ledNumber, 0x000000)
def setRightLights():
    if fwd > 0:
        set_led_color(6, rightSpeed, 0, 16711680)
        set_led_color(7, rightSpeed, 15, 16711680)
        set_led_color(8, rightSpeed, 30, 16776960)
        set_led_color(9, rightSpeed, 45, 16776960)
        set_led_color(10, rightSpeed, 60, 65280)
        set_led_color(11, rightSpeed, 75, 65280)
    else:
        set_led_color(6, rightSpeed, 0, 16711680)
        set_led_color(7, rightSpeed, 15, 16711680)
        set_led_color(8, rightSpeed, 30, 16711935)
        set_led_color(9, rightSpeed, 45, 16711935)
        set_led_color(10, rightSpeed, 60, 255)
        set_led_color(11, rightSpeed, 75, 255)
def showDirections():
    global tiltSensitivity
    tiltSensitivity = 100
    if fwd > 0:
        if right > tiltSensitivity:
            basic.show_leds("""
                . . # # #
                                . . . # #
                                . . # . #
                                . # . . .
                                # . . . .
            """)
        elif right < 0 - tiltSensitivity:
            basic.show_leds("""
                # # # . .
                                # # . . .
                                # . # . .
                                . . . # .
                                . . . . #
            """)
        else:
            basic.show_leds("""
                . . # . .
                                . # # # .
                                # . # . #
                                . . # . .
                                . . # . .
            """)
    elif right > tiltSensitivity:
        basic.show_leds("""
            # . . . .
                        . # . . .
                        . . # . #
                        . . . # #
                        . . # # #
        """)
    elif right < 0 - tiltSensitivity:
        basic.show_leds("""
            . . . . #
                        . . . # .
                        # . # . .
                        # # . . .
                        # # # . .
        """)
    else:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)

def on_received_value(name, value):
    global fwd, right
    if name == "fwd":
        fwd = value
    if name == "right":
        right = value
radio.on_received_value(on_received_value)

def setLeftLights():
    if fwd > 0:
        set_led_color(0, leftSpeed, 0, 16711680)
        set_led_color(1, leftSpeed, 15, 16711680)
        set_led_color(2, leftSpeed, 30, 16776960)
        set_led_color(3, leftSpeed, 45, 16776960)
        set_led_color(4, leftSpeed, 60, 65280)
        set_led_color(5, leftSpeed, 75, 65280)
    else:
        set_led_color(0, leftSpeed, 0, 16711680)
        set_led_color(1, leftSpeed, 15, 16711680)
        set_led_color(2, leftSpeed, 30, 16711935)
        set_led_color(3, leftSpeed, 45, 16711935)
        set_led_color(4, leftSpeed, 60, 255)
        set_led_color(5, leftSpeed, 75, 255)
leftSpeed = 0
right = 0
tiltSensitivity = 0
rightSpeed = 0
fwd = 0
radio.set_group(1)

def on_forever():
    global leftSpeed, rightSpeed
    showDirections()
    if fwd > 0:
        leftSpeed = abs(fwd + right / 2) / 1024 * 100
        rightSpeed = abs(fwd - right / 2) / 1024 * 100
        bitbot.move(BBMotor.LEFT, BBDirection.FORWARD, leftSpeed)
        bitbot.move(BBMotor.RIGHT, BBDirection.FORWARD, rightSpeed)
    else:
        leftSpeed = abs(fwd - right / 2) / 1024 * 100
        rightSpeed = abs(fwd + right / 2) / 1024 * 100
        bitbot.move(BBMotor.LEFT, BBDirection.REVERSE, leftSpeed)
        bitbot.move(BBMotor.RIGHT, BBDirection.REVERSE, rightSpeed)
    setLeftLights()
    setRightLights()
basic.forever(on_forever)
