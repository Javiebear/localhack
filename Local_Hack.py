#####################################################
# Program: Panda and Rocky
# Date: December 2, 2017
# Description: Panda flying, avoiding death
# Authors: Cindy Wang, Javier Chung, Raymond Li
#####################################################

import pygame
pygame.init()
import random
WIDTH = 625
HEIGHT= 450
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

######################################################

#colors
RED  = (255,  0,  0)
BLACK= ( 0,  0,  0)
WHITE = (255,  255,  255)
BLUE = (131, 206, 247)
GREEN = (147, 226, 177)
GRAY = (152, 155, 160)
PINK = (255, 0, 123)
PURPLE = (135, 28, 133)

x1 = 625
x2 = 625
x3 = 625
x4 = 625
x5 = 625
x6 = 625
x7 = 625

y1 = random.randint(1,HEIGHT)
y2 = random.randint(1,HEIGHT)
y3 = random.randint(1,HEIGHT)
y4 = random.randint(1,HEIGHT)
y5 = random.randint(1,HEIGHT)
y6 = random.randint(1,HEIGHT)
y7 = random.randint(1,HEIGHT)

pandaX = 0
pandaY = HEIGHT/2
speedY = 6
speedX = 6
inPlay = True

#list for xy of rocks
rock_list = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
delay = 0

#background
while inPlay:

    gameWindow.fill(WHITE)
    #check for death
    #checkdeath()


    #hitbox
    pygame.draw.rect(gameWindow, BLACK,(pandaX + 47,pandaY,50,20))
    #panda and panda movements + background

    bamboo = pygame.image.load("bambo.jpg")
    gameWindow.blit(bamboo, (0,0))

    # polling keys
    #panda
    panda = pygame.image.load("panda.png")
    gameWindow.blit(panda, (pandaX,pandaY))

    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_LEFT]:
        if pandaX > 0:
            pandaX -= speedX
    if keys[pygame.K_RIGHT]:
        if pandaX < 554:
            pandaX += speedX
    if keys[pygame.K_UP]:
        if pandaY > 0:
            pandaY -= speedY
    if keys[pygame.K_DOWN]:
        if pandaY < 411:
            pandaY += speedY



    rocky1 = pygame.image.load("Rocky2.0.png")
    gameWindow.blit(rocky1, (x1,y1))
    x1 -= 5
    rock_list[0] = ([x1,y1])
    if x1 < -50:
        y1 = random.randint(1,HEIGHT)
        x1 += 625

    rocky2 = pygame.image.load("Rocky2.0.png")
    gameWindow.blit(rocky2, (x2,y2))
    x2 -= 5
    rock_list[1] = ([x2,y2])
    if x2 < -50:
        y2 = random.randint(1,HEIGHT)
        x2 += 625

    rocky3 = pygame.image.load("Rocky2.0.png")
    gameWindow.blit(rocky3, (x3,y3))
    x3 -= 5
    rock_list[2] = ([x3,y3])
    if x3 < -50:
        y3 = random.randint(1,HEIGHT)
        x3 += 625

    rocky4 = pygame.image.load("Rocky2.0.png")
    gameWindow.blit(rocky4, (x4,y4))
    x4 -= 5
    rock_list[3] = ([x4,y4])
    if x4 < -50:
        y4 = random.randint(1,HEIGHT)
        x4 += 625

    rocky5 = pygame.image.load("Rocky2.0.png")
    gameWindow.blit(rocky5, (x5,y5))
    x5 -= 5
    rock_list[4] = ([x5,y5])
    if x5 < -50:
        y5 = random.randint(1,HEIGHT)
        x5 += 625

    rocky6 = pygame.image.load("Rocky2.0.png")
    gameWindow.blit(rocky6, (x6,y6))
    x6 -= 5
    rock_list[5] = ([x6,y6])
    if x6 < -50:
        y6 = random.randint(1,HEIGHT)
        x6 += 625

    rocky7 = pygame.image.load("Rocky2.0.png")
    gameWindow.blit(rocky7, (x7,y7))
    x7 -= 5
    rock_list[6] = ([x7,y7])
    if x7 < -50:
        y7 = random.randint(1,HEIGHT)
        x7 += 625

    if (pandaX + 47 == rock_list[0][0] and pandaY == rock_list[0][1]) or (pandaX + 47 == rock_list[1][0] and pandaY == rock_list[1][1]) or (pandaX + 47 == rock_list[2][0] and pandaY == rock_list[2][1]) or (pandaX + 47 == rock_list[3][0] and pandaY == rock_list[3][1]) or (pandaX + 47 == rock_list[4][0] and pandaY == rock_list[4][1]) or (pandaX + 47 == rock_list[5][0] and pandaY == rock_list[5][1]) or (pandaX + 47 == rock_list[6][0] and pandaY == rock_list[6][1]):
        inPlay = False

    pygame.display.update()
pygame.display.quit()
