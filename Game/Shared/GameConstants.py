__author__ = 'timotei'
import pygame
import os



class GameConstants:

    #Global Constants
    SCREEN_SIZE = [800, 400]  # WIDTH, HEIGHT
    screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]), 0, 32)
    BASIC_FONT = pygame.font.init()

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
    P1_MONSTER1_HP = 100
    P1_MONSTER1_AVATAR = pygame.image.load((os.path.join("Assets", "kurama.jpg")))
    P1_MONSTER1_AVATAR_RES = pygame.transform.scale(P1_MONSTER1_AVATAR, (200, 150))

    #  Player 2
    P2_NAME = "Flavius"
    P2_MONSTER1_HP = 150
    P2_MONSTER1_AVATAR = pygame.image.load((os.path.join("Assets", "Sasuke-Susanoo.jpg")))
    P2_MONSTER1_AVATAR_RES = pygame.transform.scale(P2_MONSTER1_AVATAR, (200, 150))
