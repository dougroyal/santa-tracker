from time import sleep
import sys
from os.path import join, dirname, realpath

import pkg_resources
import pygame
from pygame.locals import *


def main():
    print('Santa Tracker 3000')

    pygame.init()

    north_poll_img_path = pkg_resources.resource_filename('santa_tracker', join('data', 'north_poll.bmp'))
    # north_poll_img = pygame.image.load(north_poll_img_path)
    ship = pygame.image.load(north_poll_img_path)

    screen = pygame.display.set_mode((320, 240), pygame.FULLSCREEN)
    ship_top = screen.get_height() - ship.get_height()
    ship_left = screen.get_width()/2 - ship.get_width()/2

    screen.blit(ship, (ship_left, ship_top))

    # pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    pygame.display.set_caption('Santa Tracker 3000')
    while True:

        sleep(.25)
        for event in pygame.event.get():
            if event.type == QUIT:
                _quit(pygame, sys)

            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                _quit(pygame, sys)

            elif event.type == KEYDOWN and event.key == K_0:
                print('key 0')

        pygame.display.update()


def _quit(pygame, sys):
    pygame.quit()
    sys.exit()

