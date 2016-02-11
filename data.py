# -*- coding: utf-8 -*-

import sys, pygame
from pygame.locals import * 
from function import *

pygame.init()

size = width, height = 1400, 700
black = 0, 0, 0

screen = pygame.display.set_mode(size)


ball = pygame.image.load("image4.bmp").convert()
window = pygame.image.load("image5.bmp").convert()
hero = pygame.image.load("hero.png").convert()
hero.set_colorkey((0,0,0))
#hero = pygame.transform.rotate(hero, 50)
#ball = pygame.transform.rotate(ball, 50)
#window = pygame.transform.rotate(window, 50)
x, y = 0, 0
yellow    = (255, 255,   0)