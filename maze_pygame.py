from pygame import *
# from pygame.sprite import _Group

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60, 60))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            image1 = 'pacman_left (1).png'
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 60: #1235
            image1 = 'pacman_right (1).png'
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            image1 = 'pacman_up (1).png'
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height -60: #745:
            image1 = 'pacman_down (1).png'
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update1(self):
        if self.rect.x <= 1060:
            self.direction = "right"
        if self.rect.x >= win_width - 90:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update2(self):
        if self.rect.x <= 730:
            self.direction = "right"
        if self.rect.x >= 850:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    def update3(self):
        if self.rect.x <= 410:
            self.direction = "right"
        if self.rect.x >= 550:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


x1, y1 = 20, 20
x2, y2 = 1150, 250
x3, y3 = 1150, 100
x4, y4 = 815, 55
x5, y5 = 410, 500
x6, y6 = 130, 600

win_width = 1280
win_height = 700 #800

window = display.set_mode((1280, 700))
display.set_caption("Лабіринт")
background = transform.scale(image.load("bg.jpg"), (1280, 700))

font.init()
font1 = font.Font(None, 200)
win = font1.render('''           You win             ''', True, (0, 255, 0), (255, 255, 255))
lose = font1.render('''         You lose             ''', True, (255, 0, 0), (255, 255, 255))

# win = transform.scale(image.load("win.png"), (900, 500))
# lose = transform.scale(image.load("lose.png"), (900, 500))

image1 = 'pacman_right (1).png'

player = Player(image1, x1, y1, 4)
enemy = Enemy('eneemy1.png', x2, y2, 1)
enemy2 = Enemy('eneemy2.png', x4, y4, 0.6)
enemy3 = Enemy('eneemy3.png', x5, y5, 1)
treasure = GameSprite('coinn.png', x3, y3, 0)
key_pic = GameSprite('cherry.png', x6, y6, 0)

mixer.init()
mixer.music.load('gamemusic.ogg')
mixer.music.play()

money = mixer.Sound('win_sound.ogg')
kick  = mixer.Sound('kick.ogg')
key_sound = mixer.Sound('key_sound.ogg')

w1 = Wall(255, 255, 255, 100, 20, 1160, 10)
w2 = Wall(255, 255, 255, 200, 480, 315, 10)
w3 = Wall(255, 255, 255, 100, 20, 10, 380)
w4 = Wall(255, 255, 255, 200, 130, 10, 350)
w5 = Wall(255, 255, 255, 450, 130, 10, 360)
w6 = Wall(255, 255, 255, 300, 20, 10, 350)
w7 = Wall(255, 255, 255, 410, 120, 90, 10)
w8 = Wall(255, 255, 255, 100, 500, 10, 180)
w9 = Wall(255, 255, 255, 100, 770, 1160, 10)
w10 = Wall(255, 255, 255, 100, 580, 300, 10)
w11 = Wall(255, 255, 255, 390, 580, 10, 100)
w12 = Wall(255, 255, 255, 100, 680, 1160, 10)
w13 = Wall(255, 255, 255, 515, 480, 10, 210)
w14 = Wall(255, 255, 255, 510, 20, 10, 50)
w15 = Wall(255, 255, 255, 615, 380, 10, 200)
w16 = Wall(255, 255, 255, 555, 380, 65, 10)
w17 = Wall(255, 255, 255, 555, 230, 10, 150)
w18 = Wall(255, 255, 255, 555, 230, 65, 10)
w19 = Wall(255, 255, 255, 615, 30, 10, 210)
w20 = Wall(255, 255, 255, 715, 130, 10, 550)
w21 = Wall(255, 255, 255, 720, 210, 200, 10)
w22 = Wall(255, 255, 255, 820, 20, 10, 100)
w23 = Wall(255, 255, 255, 920, 120, 10, 100)
w24 = Wall(255, 255, 255, 1050, 20, 10, 350)
w25 = Wall(255, 255, 255, 820, 310, 430, 10)#
w26 = Wall(255, 255, 255, 820, 310, 10, 270)
w27 = Wall(255, 255, 255, 820, 580, 330, 10)
w28 = Wall(255, 255, 255, 920, 480, 330, 10)
w29 = Wall(255, 255, 255, 950, 430, 10, 50)
w30 = Wall(255, 255, 255, 1250, 20, 10, 660)

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
        player.update()
        enemy.update1()
        enemy2.update2()
        enemy3.update3()

        player.reset()
        enemy.reset()
        enemy2.reset()
        enemy3.reset()
        treasure.reset()
        key_pic.reset()

    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    w6.draw_wall()
    w7.draw_wall()
    w8.draw_wall()
    w9.draw_wall()
    w10.draw_wall()
    #w11.draw_wall()
    w12.draw_wall()
    w13.draw_wall()
    #w14.draw_wall()
    w15.draw_wall()
    w16.draw_wall()
    w17.draw_wall()
    w18.draw_wall()
    w19.draw_wall()
    w20.draw_wall()
    w21.draw_wall()
    w22.draw_wall()
    w23.draw_wall()
    w24.draw_wall()
    w25.draw_wall()
    w26.draw_wall()
    w27.draw_wall()
    w28.draw_wall()
    w29.draw_wall()
    w30.draw_wall()

    if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, enemy2) or sprite.collide_rect(player, enemy3) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w12) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w12) or sprite.collide_rect(player, w13) or sprite.collide_rect(player, w15) or sprite.collide_rect(player, w16) or sprite.collide_rect(player, w17) or sprite.collide_rect(player, w18) or sprite.collide_rect(player, w19)or sprite.collide_rect(player, w20)or sprite.collide_rect(player, w21)or sprite.collide_rect(player, w22)or sprite.collide_rect(player, w23)or sprite.collide_rect(player, w24)or sprite.collide_rect(player, w25)or sprite.collide_rect(player, w26)or sprite.collide_rect(player, w27)or sprite.collide_rect(player, w28)or sprite.collide_rect(player, w29)or sprite.collide_rect(player, w30):
        finish = True
        window.blit(lose, (0, 300))
        kick.play()

    if sprite.collide_rect(player, key_pic):
        w25 = Wall(255, 255, 255, 820, 310, 230, 10)
        key_pic = GameSprite('cherry.png', 1, 1000, 0)
        key_sound.play()

    if sprite.collide_rect(player, treasure):
        finish = True
        window.blit(win, (0, 300))
        money.play()
 
    display.update()
    clock.tick(FPS)