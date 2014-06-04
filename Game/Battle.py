__author__ = 'timotei'
import pygame, pygame.font, pygame.event, pygame.draw

from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants
from Game.Shared import inputbox


class Battle:

    def __init__(self):

        self.__Player1Gold = GameConstants.BUDGET
        self.__Player1Name = GameConstants.P1_NAME  # input NAME
        self.__Player1Choice1 = player_1((GameConstants.SCREEN_SIZE[0] / 2,
                                    GameConstants.SCREEN_SIZE[1] - GameConstants.MONSTER_PIC[1]),
                                    pygame.image.load(GameConstants.MONSTER_AVATAR))  # input function

        self.__Player1Choice2 = GameConstants.P1_Choice2  # input function

        self.__Player2Gold = GameConstants.BUDGET
        self.__Player2Name = GameConstants.P2_NAME  # input NAME
        self.__Player2Choice1 = GameConstants.P2_Choice1  # input function


        self.__Player2Choice2 = GameConstants.P2_Choice2  # input function

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

            #  self.screen.fill((0, 0, 0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()


            GameConstants.screen.blit(GameConstants.background, (0, 0))
            pygame.draw.line(GameConstants.screen, GameConstants.line_color, GameConstants.pos1, GameConstants.pos2, 6)


            pygame.display.update()

    def changeScene(self, scene):
        self.__currentScene = scene

    ###########
    ##Player1##
    ###########
    def Player1Gold(self):
        return self.__Player1Gold

    def getPlayer1_Monster1_HP(self):
        return self.getPlayer1_Monster1_HP

    def getPlayer1_Monster1_Attack(self):
        return self.getPlayer1_Monster1_Attack

    def getPlayer1_Monster1_SpAttack(self):
        return self.getPlayer1_Monster1_SpAttack

    def getPlayer1_Monster1_Armor(self):
        return self.getPlayer1_Monster1_Armor()

    def getPlayer1_Monster1_Avatar(self):
        return self.getPlayer1_Monster1_Avatar()

    #Monster2
    def getPlayer1_Monster2_HP(self):
        return self.getPlayer1_Monster2_HP()

    def getPlayer1_Monster2_Attack(self):
        return self.getPlayer1_Monster2_Attack()

    def getPlayer1_Monster2_SpAttack(self):
        return self.getPlayer1_Monster2_SpAttack()

    def getPlayer1_Monster2_Armor(self):
        return self.getPlayer1_Monster2_Armor()

    def getPlayer1_Monster2_Avatar(self):
        return self.getPlayer1_Monster2_Avatar()

    ###########
    ##Player2##
    ###########
    def Player2Gold(self):
        return self.Player2Gold()

    def getPlayer2_Monster1_HP(self):
        return self.getPlayer2_Monster1_HP()

    def getPlayer2_Monster1_Attack(self):
        return self.getPlayer2_Monster1_Attack()

    def getPlayer2_Monster1_SpAttack(self):
        return self.getPlayer2_Monster1_SpAttack()

    def getPlayer2_Monster1_Armor(self):
        return self.getPlayer2_Monster1_Armor()

    def getPlayer2_Monster1_Avatar(self):
        return self.getPlayer2_Monster1_Avatar()

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

    ### Other things
    def reset(self):
        pass

    def playSound(self, soundClip):
        sound = self.__sound[soundClip]

        sound.stop()
        sound.play()

Battle().start()
