__author__ = 'timotei'
import pygame
import os
import random



class GameConstants:

    #Global Constants
    SCREEN_SIZE = [800, 400]  # WIDTH, HEIGHT
    screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]), 0, 32)
    BASIC_FONT = pygame.font.init()

    #Lines Variables
    line_color = (250, 250, 250)
    pos1 = (SCREEN_SIZE[0] / 2, 0)
    pos2 = (SCREEN_SIZE[0] / 2, SCREEN_SIZE[1])

    #SOUND
    BG_SOUND = os.path.join("Assets", "soundtrack.mp3")


    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((140, 140, 140))

    MONSTER_ATTACK = [100, 150, 200]
    BUDGET = 1000
    MONSTER_PIC = [100, 100]

    #  Player 1
    P1_NAME = "Player1"
    P1_MONSTER1_AVATAR = pygame.image.load((os.path.join("Assets", "kurama.jpg")))
    P1_MONSTER1_AVATAR_RES = pygame.transform.scale(P1_MONSTER1_AVATAR, (200, 150))
    P1_TURN = ""
    P1_INDICATOR = pygame.image.load((os.path.join("Assets", "greenindicator.png")))

    #  Player 2
    P2_NAME = "Player2"
    P2_MONSTER1_AVATAR = pygame.image.load((os.path.join("Assets", "Sasuke-Susanoo.jpg")))
    P2_MONSTER1_AVATAR_RES = pygame.transform.scale(P2_MONSTER1_AVATAR, (200, 150))
    P2_INDICATOR = pygame.image.load((os.path.join("Assets", "greenindicator.png")))


    # Monsters

    # Kurama
    KURAMA_HP = 1800
    KURAMA_ATTACK = 200
    KURAMA_BLOCK = " 90 %"
    KURAMA_SP_ATTACK = 300
    KURAMA_SP_ATTACK_COST = 0.4 * KURAMA_HP

    # Susanoo
    SUSANOO_HP = 1000
    SUSANOO_ATTACK = 150
    SUSANOO_BLOCK = " 75 %"
    SUSANOO_SP_ATTACK = 250
    SUSANOO_SP_ATTACK_COST = 0.3 * SUSANOO_HP
