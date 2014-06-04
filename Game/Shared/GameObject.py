__author__ = 'timotei'


class GameObject:

    def __init__(self, position, size, sprite):
        self.__position = position
        self.__size = size
        self.__sprite = sprite

    def setPostition(self, position):
        self.__position = position

    def getPostition(self):
        return self.__position

    def getSize(self):
        return self.__size

    def getSprite(self):
        return self.__sprite
