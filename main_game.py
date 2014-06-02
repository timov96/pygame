__author__ = 'timotei'

import pygame, sys
from pygame.locals import *

pygame.init()

#Global Constants
WIDTH = 500
HEIGHT = 360
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)


#Lines Variables
line_color = (250, 250, 250)
pos1 = (WIDTH/2, 0)
pos2 = (WIDTH/2, HEIGHT)

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((140, 140, 140))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))

    screen.lock()
    pygame.draw.line(screen, line_color, pos1, pos2, 6)
    screen.unlock()


    pygame.display.update()