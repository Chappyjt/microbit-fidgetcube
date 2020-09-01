def on_button_pressed_a():
    basic.show_leds("""
        # # . . .
        # # . . .
        # # # # .
        # # # # .
        # # # # .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
    music.play_melody("E B C5 A B G A F ", 120)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_leds("""
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # # # .
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . # # # .
        # . . . #
        # # # # #
        # . . . #
        # . . . #
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    """)