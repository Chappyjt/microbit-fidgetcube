input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        # # . . .
        # # . . .
        # # # # .
        # # # # .
        # # # # .
        `)
})
input.onGesture(Gesture.Shake, function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    music.playMelody("E B C5 A B G A F ", 120)
})
input.onButtonPressed(Button.AB, function () {
    basic.showLeds(`
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # # # .
        `)
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . # # # .
        # . . . #
        # # # # #
        # . . . #
        # . . . #
        `)
})
basic.showLeds(`
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    `)
