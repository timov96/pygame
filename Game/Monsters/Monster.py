__author__ = 'timotei'

from Game.Shared import GameObject
from Game.Shared import GameConstants


class Monster(GameObject):

    def __init__(self, position, sprite, game):
        self.__game = game
        self.__HP = 500
        self.__Cost = 100
        super(Monster, self).__init__(position, GameConstants.MONSTER_PIC, sprite)

    def getGame(self):
        return self.__game

    def isDead(self):
        return self.__HP <= 0

    def getHP(self):
        return self.__HP

