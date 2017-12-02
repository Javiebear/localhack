#####################################################
# Program:
# Date: December 2
# Description: Panda flying, avoiding death, and eating bamboo
# Authors: Cindy Wang, Javier Chung, Raymond Li
#####################################################

import pygame
pygame.init()
WIDTH = 800
HEIGHT= 600
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


pandaX = 0
pandaY = HEIGHT/2
speedY = 4
speedX = 4

#background
while True:
    #panda and panda movements + background
    '''
    gameWindow.fill(WHITE)
    bamboo = pygame.image.load("bamboo.png")
    gameWindow.blit(bamboo, (0,0))
    '''
    panda = pygame.image.load("panda.png")
    gameWindow.blit(panda, (pandaX,pandaY))

# polling keys
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
    if keys[pygame.K_LEFT]:
        pandaX -= speedX
    if keys[pygame.K_RIGHT]:
        pandaX += speedX
    if keys[pygame.K_UP]:
        pandaY -= speedY
    if keys[pygame.K_DOWN]:
        pandaY += speedY

    font1 = pygame.font.SysFont(arial, 24)
    graphics = font1.render('Hello world!', 1, BLACK)
    gameWindow.blit(graphics, (200, 200))
    pygame.time.delay(10)

    pygame.display.update()
pygame.display.quit()


'''C:\Python27
#LOGIC

def checkdeath():
    while True:
        if death == 1:
            pygame.display.quit()
'''
