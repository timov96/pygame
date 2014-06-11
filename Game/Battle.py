__author__ = 'timotei'
import pygame

import os
from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants
from Game.Buttons import pygbutton


###########
##Player1##
###########
def getPlayer1_Name():
    font = pygame.font.Font(None, 30)
    text = font.render(str(GameConstants.P1_NAME), 1, (0, 255, 0))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 32, GameConstants.SCREEN_SIZE[1] / 1.1))


def getPlayer1_Monster1_HP():
    font = pygame.font.Font(None, 30)
    text = font.render("HP:" + str(GameConstants.KURAMA_HP), 1, (255, 0, 0))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 16, GameConstants.SCREEN_SIZE[1] / 2.5))


def getPlayer1_Monster1_Attack():  # Fix so this will work dynamically
    font = pygame.font.Font(None, 30)
    text = font.render("Att :" + str(GameConstants.KURAMA_ATTACK), 1, (0, 255, 40))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 16, GameConstants.SCREEN_SIZE[1] / 2.1))


def getPlayer1_Monster1_SpAttack():
    font = pygame.font.Font(None, 30)
    text = font.render("Sp Att :" + str(GameConstants.KURAMA_SP_ATTACK), 1, (255, 177, 40))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 16, GameConstants.SCREEN_SIZE[1] / 1.8))


def getPlayer1_Monster1_Armor():
    font = pygame.font.Font(None, 30)
    text = font.render("Block :" + str(GameConstants.KURAMA_BLOCK), 1, (165, 242, 243))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 16, GameConstants.SCREEN_SIZE[1] / 1.55))


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
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 1.85, GameConstants.SCREEN_SIZE[1] / 1.1))


def Player2Gold():
    font = pygame.font.Font(None, 30)
    text = font.render("Gold:" + str(GameConstants.BUDGET), 1, (255, 255, 0))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 1.78, GameConstants.SCREEN_SIZE[1] / 2))


def getPlayer2_Monster1_HP():
    font = pygame.font.Font(None, 30)
    text = font.render("HP:" + str(GameConstants.SUSANOO_HP), 1, (255, 0, 0))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 1.78, GameConstants.SCREEN_SIZE[1] / 2.5))
    # return getPlayer2_Monster1_HP


def getPlayer2_Monster1_Attack():
    font = pygame.font.Font(None, 30)
    text = font.render("Att :" + str(GameConstants.SUSANOO_ATTACK), 1, (0, 255, 40))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 1.78, GameConstants.SCREEN_SIZE[1] / 2.1))


def getPlayer2_Monster1_SpAttack():
    font = pygame.font.Font(None, 30)
    text = font.render("Sp Att :" + str(GameConstants.SUSANOO_SP_ATTACK), 1, (255, 177, 40))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 1.78, GameConstants.SCREEN_SIZE[1] / 1.8))


def getPlayer2_Monster1_Armor():
    font = pygame.font.Font(None, 30)
    text = font.render("Block :" + str(GameConstants.SUSANOO_BLOCK), 1, (165, 242, 243))
    GameConstants.screen.blit(text, (GameConstants.SCREEN_SIZE[0] / 1.78, GameConstants.SCREEN_SIZE[1] / 1.55))


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


# Sound
pygame.mixer.init()
pygame.mixer.music.load(GameConstants.BG_SOUND)
pygame.mixer.music.play(loops=-1)

# Buttons
P1_SPECIAL_ATTACK = pygbutton.PygButton((197, 300, 200, 30), ' Special Attack')
P1_ATTACK = pygbutton.PygButton((0, 300, 200, 30), 'Attack')

P2_SPECIAL_ATTACK = pygbutton.PygButton((405, 300, 200, 30), ' Special Attack')
P2_ATTACK = pygbutton.PygButton((600, 300, 200, 30), 'Attack')


# Start game

def game_start():
        GameConstants.P1_TURN = True

        while GameConstants.P1_TURN:
            GameConstants.screen.blit(GameConstants.P1_INDICATOR, (GameConstants.SCREEN_SIZE[0] / 8, GameConstants.SCREEN_SIZE[1] / 1.14))


            P1_ATTACK.draw(GameConstants.screen)
            P1_SPECIAL_ATTACK.draw(GameConstants.screen)

            P2_ATTACK.draw(GameConstants.screen)
            P2_SPECIAL_ATTACK.draw(GameConstants.screen)

            GameConstants.P1_TURN = False


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



    def start(self):
        while True:
            self.__clock.tick(30)

            #  self.screen.fill((0, 0, 0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()


            GameConstants.screen.blit(GameConstants.background, (0, 0))
            pygame.draw.line(GameConstants.screen, GameConstants.line_color, GameConstants.pos1, GameConstants.pos2, 6)

            # Adding the text and pictures for Player1
            getPlayer1_Monster1_Avatar()
            getPlayer1_Monster1_Armor()
            getPlayer1_Monster1_Attack()
            getPlayer1_Monster1_SpAttack()
            getPlayer1_Monster1_HP()
            getPlayer1_Name()


            # Adding the text and pictures for Player2
            getPlayer2_Monster1_Avatar()
            getPlayer2_Monster1_Armor()
            getPlayer2_Monster1_Attack()
            getPlayer2_Monster1_SpAttack()
            getPlayer2_Monster1_HP()
            getPlayer2_Name()

            game_start()

            pygame.display.update()

    def changeScene(self, scene):
        self.__currentScene = scene

    ### Other things
    def reset(self):
        pass


Battle().start()
