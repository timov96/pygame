__author__ = 'timotei'
import pygame

from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants


class Breakout:

    def __init__(self):
        '''
        self.__Player1Gold = GameConstants.BUDGET
        self.__Player1Name = GameConstants.P1_NAME  # input NAME
        self.__Player1Choice1 = GameConstants.P1_Choice1  # input function
        self.__Player1Choice2 = GameConstants.P1_Choice2  # input function

        self.__Player2Gold = GameConstants.BUDGET
        self.__Player2Name = GameConstants.P2_NAME  # input NAME
        self.__Player2Choice1 = GameConstants.P2_Choice1  # input function
        self.__Player2Choice2 = GameConstants.P2_Choice2  # input function
        '''
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
            self.__clock.tick(60)

            self.screen.fill((0, 0, 0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()

            pygame.display.update()

    def changeScene(self, scene):
        self.__currentScene = scene

    ###########
    ##Player1##
    ###########
    def Player1Gold(self):
        pass

    def getPlayer1_Monster1_HP(self):
        pass

    def getPlayer1_Monster1_Attack(self):
        pass

    def getPlayer1_Monster1_SpAttack(self):
        pass

    def getPlayer1Monster1_Armor(self):
        pass

    #Monster2
    def getPlayer1_Monster2_HP(self):
        pass

    def getPlayer1_Monster2_Attack(self):
        pass

    def getPlayer1_Monster2_SpAttack(self):
        pass

    def getPlayer1_Monster2_Armor(self):
        pass

    ###########
    ##Player2##
    ###########
    def Player2Gold(self):
        pass

    def getPlayer2_Monster_HP(self):
        pass

    def getPlayer2_Monster1_Attack(self):
        pass

    def getPlayer2_Monster1_SpAttack(self):
        pass

    def getPlayer2Monster1_Armor(self):
        pass

    #Monster2
    def getPlayer2_Monster2_HP(self):
        pass

    def getPlayer2_Monster2_Attack(self):
        pass

    def getPlayer2_Monster2_SpAttack(self):
        pass

    def getPlayer2_Monster2_Armor(self):
        pass

    ### Other things
    def reset(self):
        pass

    def playSound(self, soundClip):
        sound = self.__sounds[soundClip]

        sound.stop()
        sound.play()

Breakout().start()
