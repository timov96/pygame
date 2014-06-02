__author__ = 'timotei'
import pygame, sys
from Game.Scenes.Scene import Scene


class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()