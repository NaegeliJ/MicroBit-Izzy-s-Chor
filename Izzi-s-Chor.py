def on_logo_pressed():
    global Song
    Song = SongPre
    radio.send_number(Song)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_received_number(receivedNumber):
    global Song
    Song = receivedNumber
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global SongPre
    if SongPre == 1:
        SongPre = NbrSong
    else:
        SongPre += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global SongPre
    if SongPre == NbrSong:
        SongPre = 1
    else:
        SongPre += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

Tmp_Song = 0
Song = 0
SongPre = 0
NbrSong = 0
NbrSong = 3
SongPre = 1
radio.set_group(1)

def on_forever():
    global Song, Tmp_Song
    if Song != 0:
        basic.show_string("Slave")
        if Song == 1:
            music.start_melody(music.built_in_melody(Melodies.NYAN), MelodyOptions.ONCE)
        elif Song == 2:
            music.start_melody(music.built_in_melody(Melodies.DADADADUM),
                MelodyOptions.ONCE)
        elif Song == 3:
            music.start_melody(music.built_in_melody(Melodies.FUNK), MelodyOptions.ONCE)
        Song = 0
    basic.show_string("" + str((SongPre)))
    if SongPre != Tmp_Song:
        if SongPre == 1:
            music.start_melody(music.built_in_melody(Melodies.NYAN), MelodyOptions.ONCE)
        elif SongPre == 2:
            music.start_melody(music.built_in_melody(Melodies.DADADADUM),
                MelodyOptions.ONCE)
        elif SongPre == 3:
            music.start_melody(music.built_in_melody(Melodies.FUNK), MelodyOptions.ONCE)
        Tmp_Song = SongPre
basic.forever(on_forever)
