Play = False
Song = 1
radio.set_group(1)

def on_received_number(receivedNumber):
    global Play, Song
    Song = receivedNumber
    Play = True


def on_button_pressed_a():
    global Song
    if Song == 3:
        Song = 1
    else:
        Song += 1


def on_button_pressed_b():
    global Play
    radio.send_number(Song)
    Play = True

radio.on_received_number(on_received_number)
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global Play, Song
    basic.show_number(Song)
    if Play == True:
        basic.show_icon(IconNames.YES)
        if Song == 1:
            music.start_melody(music.built_in_melody(Melodies.NYAN), MelodyOptions.ONCE)
        elif Song == 2:
            music.start_melody(music.built_in_melody(Melodies.DADADADUM),
                MelodyOptions.ONCE)
        elif Song == 3:
            music.start_melody(music.built_in_melody(Melodies.FUNK), MelodyOptions.ONCE)
        Play = False
basic.forever(on_forever)
