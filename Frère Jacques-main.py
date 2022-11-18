from microbit import *
import music

display.show(Image.YES)
while True:
    if button_a.was_pressed():
        display.show(Image.HEART)
        for x in range(2):
            music.play(['C4:4', 'D4', 'E4', 'C4'])
        for x in range(2):
            music.play(['E4:4', 'F4', 'G4:8'])
            
    if button_b.was_pressed():
        display.show(Image.SKULL)
        music.play(music.DADADADUM)