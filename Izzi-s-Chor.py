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

def Music_Imperial_March():
    for index in range(4):
        music.play_tone(392, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(392, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(392, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(330, music.beat(BeatFraction.QUARTER))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(294, music.beat(BeatFraction.HALF))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(330, music.beat(BeatFraction.HALF))
        music.rest(music.beat(BeatFraction.EIGHTH))
        music.play_tone(294, music.beat(BeatFraction.HALF))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        music.play_tone(523, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))

def Music_Never_Gonna():
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(415, music.beat(BeatFraction.QUARTER))
    music.play_tone(370, music.beat(BeatFraction.QUARTER))
    music.play_tone(349, music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.DOUBLE))
    music.play_tone(415, music.beat(BeatFraction.QUARTER))
    music.play_tone(370, music.beat(BeatFraction.QUARTER))
    music.play_tone(349, music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(415, music.beat(BeatFraction.QUARTER))
    music.play_tone(370, music.beat(BeatFraction.QUARTER))
    music.play_tone(349, music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.DOUBLE))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(415, music.beat(BeatFraction.WHOLE))
    music.play_tone(415, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.DOUBLE))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(233, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    music.play_tone(208, music.beat(BeatFraction.QUARTER))
    music.play_tone(277, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.QUARTER))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(233, music.beat(BeatFraction.HALF))
    music.play_tone(208, music.beat(BeatFraction.HALF))
    music.play_tone(175, music.beat(BeatFraction.HALF))
    music.play_tone(311, music.beat(BeatFraction.HALF))
    music.play_tone(277, music.beat(BeatFraction.DOUBLE))

def Music_Tetris():
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.HALF))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(349, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.HALF))
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.HALF))

def on_forever():
    global Play, Song
    basic.show_number(Song)
    if Play == True:
        basic.show_icon(IconNames.YES)
        if Song == 1:
            Music_Imperial_March()
        elif Song == 2:
            Music_Never_Gonna()
        elif Song == 3:
            Music_Tetris()
        Play = False
basic.forever(on_forever)
