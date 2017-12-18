#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Modules

#MUGEN

import math
import os
import sys, pygame
from pygame.locals import *
import random


#Constants
WIDTH = 900
HEIGHT = 600
path = os.path.join("SPRITES")

speed = 3
ammo = 10


#classes
#---------------------------------------------------------------------------------------------------------

#duck class

class Duck(pygame.sprite.Sprite):
    def __init__(self, color, direction, x, y, speed):
        pygame.sprite.Sprite.__init__(self)

        self.direction = direction
        self.dead = False
        self.color = color

        def look(self):
            if self.direction == "left":
                look = "2.png"
            elif self.direction == "right":
                look = ".png"
            return look

        self.look = self.color + look(self)
        self.image = load_image("duck_outline_target_" + self.look)
        self.rect = self.image.get_rect()
        self.target = pygame.rect.Rect((0 , 0), (50, 50))
        self.target.midbottom = self.rect.midbottom
        self.rect.centery = y
        self.rect.centerx = x
        self.speed = speed

    def increase_speed(self) :
        speed += 1


    def update(self):
        if self.rect.centerx >= 900 :
            self.__init__(self.color, "left", 900, self.rect.centery, self.speed)

        elif self.rect.centerx <= 0 :
            self.__init__(self.color, "right", 0, self.rect.centery, self.speed)


    def move(self):
        if not self.dead :
            if self.direction == "left":
                self.rect.centerx -= self.speed
                self.target.midbottom = self.rect.midbottom
            elif  self.direction == "right":
                self.rect.centerx += self.speed
                self.target.midbottom = self.rect.midbottom

    def die(self) :
        self.dead = True
        self.image = load_image("shot_grey_large.png")
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = pygame.mouse.get_pos()
        self.target = pygame.rect.Rect((0,0), (0,0))

#Mouse class

class Mouse(pygame.sprite.DirtySprite):
    def __init__(self, filename):
        super(Mouse, self).__init__()
        pygame.mouse.set_visible(0)
        self.image = load_image(filename)
        self.rect = self.image.get_rect()

    def get_pos(self):
        return pygame.mouse.get_pos()

    def set_pos(self, position):
        pygame.mouse.set_pos(position)

    def update(self):
        self.rect.center = self.get_pos()

    def is_clicked(self):
        return pygame.mouse.get_pressed()

#Gun class

class Gun(pygame.sprite.DirtySprite) :
    def __init__(self, filename) :
        super(Gun, self).__init__()
        self.image = load_image(filename)
        self.rect = self.image.get_rect()
        self.rect.centery = 600

    def aim(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.centerx = mousex + 100

#Counter class

class Counter(pygame.sprite.DirtySprite) :
    def __init__(self) :
        self.counter = 0
        self.string = str(self.counter)

    def increase(self) :
        self.counter += 1
        self.string = str(self.counter)

    def draw(self, screen, xxx_todo_changeme ) :
        (x, y) = xxx_todo_changeme
        draw_score(self.string, screen, "_small", (x, y))



#Bullet class

class Bullet(pygame.sprite.DirtySprite) :
    def __init__(self, x) :
        self.look = "silver"
        self.path = "icon_bullet_"
        self.path2 = "_long.png"
        self.image = load_image(self.path + self.look + self.path2)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = 30

    def shoot(self, x) :
        self.look = "empty"
        self.image = load_image(self.path + self.look + self.path2)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = 30


#Button Class

class Button(pygame.sprite.DirtySprite) :
    def __init__(self, caption, center) :
        self.fontpath = os.path.join(path, "fluo.ttf")
        self.font = pygame.font.Font(self.fontpath, 30)
        self.textcolor = [255, 255, 255]
        self.caption = caption
        self.textsurf, self.textrect = text_objects(caption, self.font, self.textcolor)
        self.textrect.center = center
        self.rect = self.textrect

    def draw(self, screen) :
        screen.blit(self.textsurf, self.textrect)


class Duckie(pygame.sprite.Sprite):
    def __init__(self, color, direction, x, y, speed):
        pygame.sprite.Sprite.__init__(self)

        self.direction = direction
        self.color = color

        def look(self):
            if self.direction == "left":
                look = "2.png"
            elif self.direction == "right":
                look = ".png"
            return look

        self.look = self.color + look(self)
        self.image = load_image("duck_outline_" + self.look)
        self.rect = self.image.get_rect()
        self.target = pygame.rect.Rect((0 , 0), (50, 50))
        self.target.midbottom = self.rect.midbottom
        self.rect.centery = y
        self.rect.centerx = x
        self.speed = speed


    def update(self):
        if self.rect.centerx >= 900 :
            self.__init__(self.color, "left", 900, self.rect.centery, self.speed)

        elif self.rect.centerx <= 0 :
            self.__init__(self.color, "right", 0, self.rect.centery, self.speed)


    def move(self):
            if self.direction == "left":
                self.rect.centerx -= self.speed
                self.target.midbottom = self.rect.midbottom
            elif  self.direction == "right":
                self.rect.centerx += self.speed
                self.target.midbottom = self.rect.midbottom

class Shot(pygame.sprite.DirtySprite) :
    def __init__(self, xxx_todo_changeme1) :
        (x, y) = xxx_todo_changeme1
        self.look = random.choice(["grey", "yellow"])
        self.image = load_image("shot_" + self.look + "_large.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def blit(self, screen) :

        screen.blit(self.image, self.rect)


#---------------------------------------------------------------------------------------------------------

#Functions
#---------------------------------------------------------------------------------------------------------

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def load_image(filename):
    try : image = pygame.image.load(os.path.join(path, filename))
    except pygame.error as message:
        raise SystemExit(message)
    image = image.convert_alpha()
    return image


def init_ducks(ducks, howmanyducks) :
    y = 300

    for i in range(howmanyducks) :
        x = random.randint(0, 900)
        y += 80
        direction = random.choice(["left", "right"])
        color = random.choice(["brown", "white", "yellow"])

        ducks.append(Duck(color, direction, x, y, speed))

def init_bullets(bullets, ammo) :
    x = 700

    for i in range(ammo) :

        bullets.append(Bullet(x))
        x -= 25


def draw_score(score, screen, size, xxx_todo_changeme2) :

    (x, y) = xxx_todo_changeme2
    cero = load_image("text_0" + size + ".png")
    cero_rect = cero.get_rect()

    if len(score) == 1 :
        score_img = load_image("text_" + score + size + ".png")
        screen.blit(cero, (x, y))
        x += cero_rect.right
        screen.blit(cero, (x , y))
        x += cero_rect.right
        screen.blit(score_img, (x , y))
    elif len(score) == 2 :
        score_img_0 = load_image("text_" + score[0] + size + ".png")
        score_img_0_rect = score_img_0.get_rect()
        score_img_1 = load_image("text_" + score[1] + size + ".png")
        screen.blit(cero, (x, y))
        x += cero_rect.right
        screen.blit(score_img_0, (x, y))
        x += score_img_0_rect.right
        screen.blit(score_img_1, (x, y))
    elif len(score) == 3 :
        score_img_0 = load_image("text_" + score[0] + size + ".png")
        score_img_0_rect = score_img_0.get_rect()
        score_img_1 = load_image("text_" + score[1] + size +".png")
        score_img_1_rect = score_img_1.get_rect()
        score_img_2 = load_image("text_" + score[2] + size + ".png")
        screen.blit(score_img_0, (x, y))
        x += score_img_0_rect.right
        screen.blit(score_img_1, (x, y))
        x += score_img_1_rect.right
        screen.blit(score_img_2, (x, y))


def game_over(screen, total_score, rifle) :

    #Sounds

    shoot_sound = pygame.mixer.Sound(os.path.join(path, "shot.wav"))
    shoot_sound.set_volume(0.1)

    score = "SCORE : " + str(total_score)

    quit_button = Button("MENU", (300, 500))
    restart_button = Button("RESTART", (550, 500))
    score_caption = Button(score, (WIDTH/2, HEIGHT/2))

    game_over_background = load_image("GObackground.png")

    clock = pygame.time.Clock()

    mouse = Mouse("crosshair_outline_small.png")

    shots = []

    while True :

        time = clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT :
                sys.exit(0)
            elif event.type == MOUSEBUTTONDOWN :

                shots.append(Shot(mouse.get_pos()))

                shoot_sound.play()

                if quit_button.rect.collidepoint(mouse.get_pos()) :
                    menu()
                elif restart_button.rect.collidepoint(mouse.get_pos()):
                    main(screen, rifle)

        screen.blit(game_over_background, (0,0))

        quit_button.draw(screen)
        restart_button.draw(screen)
        score_caption.draw(screen)

        mouse.update()

        for shot in shots:
            shot.blit(screen)

        screen.blit(mouse.image, mouse.rect)


        pygame.display.flip()

    return 0

def menu() :

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Duck Shooting 2.0")


    shoot_sound = pygame.mixer.Sound(os.path.join(path, "shot.wav"))
    shoot_sound.set_volume(0.1)
    menu_background = load_image("MEbackground.png")
    clock = pygame.time.Clock()
    mouse = Mouse("crosshair_outline_large.png")

    play = Button("PLAY", (300, 500))
    quit = Button("QUIT", (600, 500))
    title = Button("DUCK SHOOTING", (WIDTH/2, 300))

    x = random.randint(0, 900)
    y = 200
    direction = random.choice(["left", "right"])
    color = random.choice(["brown", "white", "yellow"])
    duck = Duckie(color, direction, x, y, 3)

    shots = []

    while True :

        time = clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT :
                sys.exit(0)
            elif event.type == MOUSEBUTTONDOWN :

                shots.append(Shot(mouse.get_pos()))

                shoot_sound.play()

                if quit.rect.collidepoint(mouse.get_pos()) :
                    sys.exit(0)
                elif play.rect.collidepoint(mouse.get_pos()):
                    gun_select(screen)

        screen.blit(menu_background, (0,0))

        quit.draw(screen)
        play.draw(screen)
        title.draw(screen)

        mouse.update()
        duck.move()
        duck.update()

        for shot in shots :
            shot.blit(screen)

        duck.speed += 0.01

        screen.blit(duck.image, duck.rect)

        screen.blit(mouse.image, mouse.rect)

        pygame.display.flip()

    return 0

def gun_select(screen) :
    shoot_sound = pygame.mixer.Sound(os.path.join(path, "shot.wav"))
    shoot_sound.set_volume(0.1)
    menu_background = load_image("MEbackground.png")
    clock = pygame.time.Clock()
    mouse = Mouse("crosshair_outline_large.png")

    subtitle = Button("SELECT YOUR WEAPON", (WIDTH/2, 200))

    rifle = load_image("rifle.png")
    rifle_rect = rifle.get_rect()
    rifle_rect.centerx, rifle_rect.centery = 300, 400

    rifle_red = load_image("rifle_red.png")
    rifle_red_rect = rifle_red.get_rect()
    rifle_red_rect.centerx, rifle_red_rect.centery = 600, 400



    while True :

        time = clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT :
                sys.exit(0)
            elif event.type == MOUSEBUTTONDOWN :

                shoot_sound.play()

                if rifle_rect.collidepoint(mouse.get_pos()) :
                    main(screen, "rifle.png")
                elif rifle_red_rect.collidepoint(mouse.get_pos()):
                    main(screen, "rifle_red.png")

        screen.blit(menu_background, (0,0))


        subtitle.draw(screen)

        screen.blit(rifle, rifle_rect)
        screen.blit(rifle_red, rifle_red_rect)

        mouse.update()

        screen.blit(mouse.image, mouse.rect)

        pygame.display.flip()

    return 0


#---------------------------------------------------------------------------------------------------------
#Main game definition

def main(screen, rifle):

    print("ENTRE A MAIN")

    global speed
    global ammo

    howmanyducks = 0
    ducks = []
    bullets = []
    speed = 3
    current = 0
    ammo = 10

    water = pygame.image.load(os.path.join(path, "water.png"))

    #main game features
    background_image = load_image("background.png")
    clock = pygame.time.Clock()

    print("Pase game features")
    #initalize classes
    ducks[:] = []
    init_ducks(ducks, howmanyducks)
    mouse = Mouse("crosshair_red_small.png")
    gun = Gun(rifle)
    total_score = Counter()
    counter = Counter()
    score = load_image("text_score_small.png")
    init_bullets(bullets, ammo)

    #Sounds
    shoot_sound = pygame.mixer.Sound(os.path.join(path, "shot.wav"))
    shoot_sound.set_volume(0.1)

    #Main Game Loop
    while True:
        if counter.counter == howmanyducks :

            counter.__init__()

            pygame.time.wait(1000)

            howmanyducks = 3
            ammo = 10
            current = 0
            speed += 1

            ducks[:] = []
            init_ducks(ducks, howmanyducks)
            bullets[:] = []
            init_bullets(bullets, ammo)

        if ammo == 0:
            game_over(screen, total_score.counter, rifle)


        time = clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == MOUSEBUTTONDOWN :

                bullets[current].shoot(bullets[current].rect.centerx)
                current += 1
                ammo -= 1
                shoot_sound.play()

                print("Is clicked!")
                for duck in ducks :
                    if duck.target.collidepoint(mouse.get_pos()):
                        if not duck.dead :
                            print("Duck dead!")
                            duck.die()
                            counter.increase()
                            total_score.increase()

        mouse.update()

        gun.aim()

        screen.blit(background_image, (0, 0))

        y = 350

        for duck in ducks :
            duck.move()
            duck.update()
            screen.blit(duck.image, duck.rect)
            screen.blit(water, (0, y))
            y += 80


        screen.blit(gun.image, gun.rect)

        screen.blit(score, (5 , 5))

        (x, y) = (5 + score.get_rect().right, 5)

        total_score.draw(screen, (x, y))

        for bullet in bullets :
            screen.blit(bullet.image, bullet.rect)

        screen.blit(mouse.image, mouse.rect)

        pygame.display.flip()

    return 0

if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    menu()
