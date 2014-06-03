###############################################
######Adapted by James Reeves from an inputbox by Timothy Downs
#http://www.pygame.org/pcr/inputbox/inputbox.py

import sys
import pygame
from pygame.locals import *


def display_box(screen, message):
    "Print a message in a box in the middle of the screen"
    font = pygame.font.Font(None, 18)
    rect = pygame.Rect([0, 0, 220, 22])
    offset = (3, 3)

    center = screen.get_rect().center
    rect.center = center

    pygame.draw.rect(screen, (0, 0, 0), rect, 0)
    pygame.draw.rect(screen, (255, 255, 255), rect, 1)

    rect.left += offset[0]
    rect.top += offset[1]

    if len(message) != 0:
        screen.blit(font.render(message, 1, (255,255,255)), rect.topleft)

    pygame.display.flip()


    def ask(screen, question):
        """ask(screen, question) -> answer"""
        pygame.font.init()
        text = ""
        display_box(screen, question + ": " + text)

        while True:
            pygame.time.wait(0)
            event = pygame.event.poll()

            if event.type == QUIT:
                sys.exit()
            if event.type != KEYDOWN:
                continue

            if event.key == K_BACKSPACE:
                text = text[0:-1]
            elif event.key == K_RETURN:
                break
            else:
                text += event.unicode.encode("ascii")

            display_box(screen, question + ": " + text)

        return text


    if __name__ == '__main__':
        pygame.init()
        screen = pygame.display.set_mode((500, 360))
        print ("'%s' was entered." % ask(screen, "Name"))