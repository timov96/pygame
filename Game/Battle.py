__author__ = 'timotei'
import pygame, pygame.font, pygame.event, pygame.draw

import os
from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants


###########
##Player1##
###########
def getPlayer1_Name():
    font = pygame.font.Font(None, 30)
    text = font.render(str(GameConstants.P1_NAME), 1, (0, 255, 0))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 32, GameConstants.SCREEN_SIZE[1] / 1.1))
    # return getPlayer1_Name()


def getPlayer1_Monster1_HP():
    font = pygame.font.Font(None, 30)
    text = font.render("HP:" + str(GameConstants.P1_MONSTER1_HP), 1, (255, 0, 0))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 16, GameConstants.SCREEN_SIZE[1] / 2.5))
    # return getPlayer1_Monster1_HP


def getPlayer1_Monster1_Attack(self):
    return self.getPlayer1_Monster1_Attack


def getPlayer1_Monster1_SpAttack(self):
    return self.getPlayer1_Monster1_SpAttack


def getPlayer1_Monster1_Armor(self):
    return self.getPlayer1_Monster1_Armor()


def getPlayer1_Monster1_Avatar():
    GameConstants.screen.blit(GameConstants.P1_MONSTER1_AVATAR_RES, (100, 1))

#Monster2


def getPlayer1_Monster2_HP(self):
    return self.getPlayer1_Monster2_HP()


def getPlayer1_Monster2_Attack(self):
    return self.getPlayer1_Monster2_Attack()


def getPlayer1_Monster2_SpAttack(self):
    return self.getPlayer1_Monster2_SpAttack()


def getPlayer1_Monster2_Armor(self):
    return self.getPlayer1_Monster2_Armor()


def getPlayer1_Monster2_Avatar():
    return getPlayer1_Monster2_Avatar()


def Player1Gold():
    font = pygame.font.Font(None, 30)
    text = font.render("Gold:" + str(GameConstants.BUDGET), 1, (255, 255, 0))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 16, GameConstants.SCREEN_SIZE[1] / 2))

###########
##Player2##
###########


def getPlayer2_Name():
    font = pygame.font.Font(None, 30)
    text = font.render(str(GameConstants.P2_NAME), 1, (0, 255, 0))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 1.78, GameConstants.SCREEN_SIZE[1] / 1.1))


def Player2Gold():
    font = pygame.font.Font(None, 30)
    text = font.render("Gold:" + str(GameConstants.BUDGET), 1, (255, 255, 0))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 1.78, GameConstants.SCREEN_SIZE[1] / 2))


def getPlayer2_Monster1_HP():
    font = pygame.font.Font(None, 30)
    text = font.render("HP:" + str(GameConstants.P2_MONSTER1_HP), 1, (255, 0, 0))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 1.78, GameConstants.SCREEN_SIZE[1] / 2.5))
    # return getPlayer2_Monster1_HP


def getPlayer2_Monster1_Attack():
    return getPlayer2_Monster1_Attack()


def getPlayer2_Monster1_SpAttack():
    return getPlayer2_Monster1_SpAttack()


def getPlayer2_Monster1_Armor():
    return getPlayer2_Monster1_Armor()


def getPlayer2_Monster1_Avatar():
    GameConstants.screen.blit(GameConstants.P2_MONSTER1_AVATAR_RES, (500, 1))

#Monster2


def getPlayer2_Monster2_HP(self):
    return self.getPlayer2_Monster2_HP()


def getPlayer2_Monster2_Attack(self):
    return self.getPlayer2_Monster2_Attack()


def getPlayer2_Monster2_SpAttack(self):
    return self.getPlayer2_Monster2_SpAttack()


def getPlayer2_Monster2_Armor(self):
    return self.getPlayer2_Monster2_Armor()


def getPlayer2_Monster2_Avatar(self):
    return self.getPlayer2_Monster2_Avatar()


###
#Actual Class Begins
###

class Battle:

    def __init__(self):

        self.__Player1Gold = GameConstants.BUDGET
        self.__Player1Name = GameConstants.P1_NAME  # input NAME
        self.__Player1Choice1 = pygame.image.load(os.path.join("Assets", "kurama.jpg"))  # input function


        self.__Player2Gold = GameConstants.BUDGET
        self.__Player2Name = GameConstants.P2_NAME  # input NAME


        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("HTS BATTLE")

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

        self.__scenes = (
            PlayingGameScene(self),
            WinnerScene(self),
            MenuScene(self),
            Player2Choosing(self),
            Player1Choosing(self)
        )

        self.__currentScene = 0

        self.__sound = ()

    def start(self):
        while True:
            self.__clock.tick(40)

            #  self.screen.fill((0, 0, 0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()


            GameConstants.screen.blit(GameConstants.background, (0, 0))
            pygame.draw.line(GameConstants.screen, GameConstants.line_color, GameConstants.pos1, GameConstants.pos2, 6)

            # Adding the text and pictures for Player1
            getPlayer1_Monster1_Avatar()
            Player1Gold()
            getPlayer1_Monster1_HP()

            getPlayer1_Name()

            # Adding the text and pictures for Player2
            getPlayer2_Monster1_Avatar()
            Player2Gold()
            getPlayer2_Monster1_HP()

            getPlayer2_Name()



            pygame.display.update()

    def changeScene(self, scene):
        self.__currentScene = scene

    ### Other things
    def reset(self):
        pass

    def playSound(self, soundClip):
        sound = self.__sound[soundClip]

        sound.stop()
        sound.play()

Battle().start()
