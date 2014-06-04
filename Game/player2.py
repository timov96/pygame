__author__ = 'timotei'

import pygame
from Game.Shared import *


class player2(GameObject):

    def __init__(self, name_p2, gold, monster1, monster2, game):
        self.__game = game
        self.__monster1 = GameConstants.P2_Choice1
        self.__monster2 = GameConstants.P2_Choice2
        self.__name_p2 = GameConstants.P1_NAME
        self.__gold = GameConstants.BUDGET

        super(player2, self).__init__(0, 0, 0)

    def set_p2_name(self):
        return self.__gold

    def set_p2_choice1(self):
        return self.__monster1

    def set_p2_choice2(self):
        return self.__monster2

    def get_p2_gold(self):
        return self.__gold