__author__ = 'timotei'
import pygame, sys
from Game.Scenes.Scene import Scene


class PlayingGameScene(Scene):

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.getGame()

        player1 = game.getPosition(10, 10)
        game.screen.blit(player1.getSprite(), player1.getPostition())


    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()