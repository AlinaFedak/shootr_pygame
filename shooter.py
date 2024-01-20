from pygame import *
from random import randint
# from pygame.sprite import _Group

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (100, 100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > -10:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 90: #1235
            self.rect.x += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > -10:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < win_width - 90: #1235
            self.rect.x += self.speed
    def fire(self):
        pass

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width-80)
            self.rect.y = 0
            lost = lost + 1

win_width = 1280
win_height = 700

x1, y1 = win_width/2+200, win_height-100
x2, y2 = win_width/2-300, win_height-100

window = display.set_mode((win_width, win_height))
display.set_caption("Шутер")
background = transform.scale(image.load("starry_sky.png"), (win_width, win_height))

player = Player('rocket.png', x1, y1, 4)
player2 = Player('rocket2.png', x2, y2, 4)

monsters = sprite.Group()

mixer.init()
mixer.music.load('destination.ogg')
mixer.music.play()

fire = mixer.Sound('fire_sound.ogg')

clock = time.Clock()
FPS = 60

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
           game = False
    if finish != True:
        window.blit(background, (0,0))
        player.update1()
        player2.update2()

        player.reset()
        player2.reset()

    display.update()
    time.delay(30)
    # clock.tick(FPS)