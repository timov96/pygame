__author__ = 'timotei'

import pygame
from Game.Shared import *


class player1(GameObject):

    def __init__(self, player_1, gold, monster1, monster2, game):
        self.__game = game
        self.__monster1 = GameConstants.P1_Choice1
        self.__monster2 = GameConstants.P1_Choice2
        self.__player_1 = GameConstants.P1_NAME
        self.__gold = GameConstants.BUDGET

        super(player1, self).__init__(0, 0, 0)

    def set_p1_name(self):
        return self.__player_1

    def set_p1_choice1(self):
        return self.__monster1

    def set_p1_choice2(self):
        return self.__monster2

    def get_p1_gold(self):
        return self.__gold
