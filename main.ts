function set_led_color (ledNumber: number, incoming_speed: number, threshold: number, colour: number) {
    if (incoming_speed > threshold) {
        bitbot.setPixelColor(ledNumber, colour)
    } else {
        bitbot.setPixelColor(ledNumber, 0x000000)
    }
}
function setRightLights () {
    if (fwd > 0) {
        set_led_color(6, rightSpeed, 0, 16711680)
        set_led_color(7, rightSpeed, 15, 16711680)
        set_led_color(8, rightSpeed, 30, 16776960)
        set_led_color(9, rightSpeed, 45, 16776960)
        set_led_color(10, rightSpeed, 60, 65280)
        set_led_color(11, rightSpeed, 75, 65280)
    } else {
        set_led_color(6, rightSpeed, 0, 16711680)
        set_led_color(7, rightSpeed, 15, 16711680)
        set_led_color(8, rightSpeed, 30, 16711935)
        set_led_color(9, rightSpeed, 45, 16711935)
        set_led_color(10, rightSpeed, 60, 255)
        set_led_color(11, rightSpeed, 75, 255)
    }
}
function showDirections () {
    tiltSensitivity = 100
    if (fwd > 0) {
        if (right > tiltSensitivity) {
            basic.showLeds(`
                . . # # #
                . . . # #
                . . # . #
                . # . . .
                # . . . .
                `)
        } else if (right < 0 - tiltSensitivity) {
            basic.showLeds(`
                # # # . .
                # # . . .
                # . # . .
                . . . # .
                . . . . #
                `)
        } else {
            basic.showLeds(`
                . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
                `)
        }
    } else if (right > tiltSensitivity) {
        basic.showLeds(`
            # . . . .
            . # . . .
            . . # . #
            . . . # #
            . . # # #
            `)
    } else if (right < 0 - tiltSensitivity) {
        basic.showLeds(`
            . . . . #
            . . . # .
            # . # . .
            # # . . .
            # # # . .
            `)
    } else {
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
    }
}
radio.onReceivedValue(function (name, value) {
    if (name == "fwd") {
        fwd = value
    }
    if (name == "right") {
        right = value
    }
})
function setLeftLights () {
    if (fwd > 0) {
        set_led_color(0, leftSpeed, 0, 16711680)
        set_led_color(1, leftSpeed, 15, 16711680)
        set_led_color(2, leftSpeed, 30, 16776960)
        set_led_color(3, leftSpeed, 45, 16776960)
        set_led_color(4, leftSpeed, 60, 65280)
        set_led_color(5, leftSpeed, 75, 65280)
    } else {
        set_led_color(0, leftSpeed, 0, 16711680)
        set_led_color(1, leftSpeed, 15, 16711680)
        set_led_color(2, leftSpeed, 30, 16711935)
        set_led_color(3, leftSpeed, 45, 16711935)
        set_led_color(4, leftSpeed, 60, 255)
        set_led_color(5, leftSpeed, 75, 255)
    }
}
let leftSpeed = 0
let right = 0
let tiltSensitivity = 0
let rightSpeed = 0
let fwd = 0
radio.setGroup(1)
basic.forever(function () {
    showDirections()
    if (fwd > 0) {
        leftSpeed = Math.abs(fwd + right / 2) / 1024 * 100
        rightSpeed = Math.abs(fwd - right / 2) / 1024 * 100
        bitbot.move(BBMotor.Left, BBDirection.Forward, leftSpeed)
        bitbot.move(BBMotor.Right, BBDirection.Forward, rightSpeed)
    } else {
        leftSpeed = Math.abs(fwd - right / 2) / 1024 * 100
        rightSpeed = Math.abs(fwd + right / 2) / 1024 * 100
        bitbot.move(BBMotor.Left, BBDirection.Reverse, leftSpeed)
        bitbot.move(BBMotor.Right, BBDirection.Reverse, rightSpeed)
    }
    setLeftLights()
    setRightLights()
})
