__author__ = 'timotei'
import pygame


class GameConstants:

    #Global Constants
    SCREEN_SIZE = [500, 360]  # WIDTH, HEIGHT
    screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]), 0, 32)

    #Lines Variables
    line_color = (250, 250, 250)
    pos1 = (SCREEN_SIZE[0] / 2, 0)
    pos2 = (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1])

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((140, 140, 140))

    MONSTER_ATTACK = [100, 150, 200]
    BUDGET = 1000
    MONSTER_PIC = [100, 100]

    #  Player 1
    P1_NAME = "Timotei"
    P1_Choice1 = "Kurama"
    P1_Choice2 = "Susanoo"

    #  Player 2
    P2_NAME = "Flavius"
    P2_Choice1 = "Kurama"
    P2_Choice2 = "Susanoo"