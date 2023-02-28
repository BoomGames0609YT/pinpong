from pygame import *
win_w = 700
win_h = 500
clock = time.Clock()
FPS = 60
win = display.set_mode((win_w, win_h))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, sizw_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect - self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed


    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed




game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game == False


    win.fill((100,100,100))
    
    display.update()
    clock.tick(FPS)

