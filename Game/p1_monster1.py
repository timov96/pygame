__author__ = 'timotei'

from Game.Shared import *


class p1_monster1(GameObject):

    def __init__(self, position, sprite):
        super(p1_monster1, self).__init__(position, GameConstants.MONSTER_AVATAR, sprite)

    def setPosition(self, position):

        newPosition = [position[0], position[1]]
        size = self.getSize()

        # if newPosition[0] + size[0] > GameConstants.SCREEN_SIZE[0]:
        #    newPosition[0] = GameConstants.SCREEN_SIZE[0] - size[0]

        super(p1_monster1, self).setPosition(newPosition)