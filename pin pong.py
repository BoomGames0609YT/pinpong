from pygame import *
win_w = 700
win_h = 500
clock = time.Clock()
FPS = 60
win = display.set_mode((win_w, win_h))
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game == False


    win.fill((100,100,100))
    
    display.update()
    clock.tick(FPS)
