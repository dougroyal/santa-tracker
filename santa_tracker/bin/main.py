from time import sleep
import sys
from os import listdir
from os.path import join, dirname, realpath

import pkg_resources
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE


def main():
    print('Santa Tracker 3000')
    pygame.init()
    pygame.display.set_caption('Santa Tracker 3000')
    # screen = pygame.display.set_mode((320, 240))
    screen = pygame.display.set_mode((320, 240), pygame.FULLSCREEN)

    img_dir = pkg_resources.resource_filename('santa_tracker', 'data')
    images = [pygame.image.load(join(img_dir, file_name)) for file_name in listdir(img_dir) if file_name.endswith('.bmp')]

    _load_image(screen, images[0])

    while True:

        sleep(.25)
        for event in pygame.event.get():
            if event.type == QUIT:
                _quit(pygame, sys)

            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                _quit(pygame, sys)

            elif event.type == KEYDOWN:
                try:
                    index = int(chr(event.key)) - 1
                    if index <= len(images):
                        _load_image(screen, images[index])
                except:
                    # They pressed an invalid key
                    pass


def _get_img_path(file_name):
    return pkg_resources.resource_filename('santa_tracker', join('data', file_name))


def _load_image(screen, img):
    img_top = screen.get_height() - img.get_height()
    img_left = screen.get_width()/2 - img.get_width()/2
    screen.blit(img, (img_left, img_top))
    pygame.display.update()


def _quit(pygame, sys):
    pygame.quit()
    sys.exit()

