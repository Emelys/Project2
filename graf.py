# -*- coding: utf-8 -*-

import sys, pygame
from pygame.locals import * 
from function import *
from data import *

pygame.init()

screen = pygame.display.set_mode(size)


def create_field(texture_size):
    screen.fill(black)
    for i in range(0, width // texture_size):
        for j in range(0, width // texture_size):
            if i % 2 == 0 or j % 2 == 0:
                screen.blit(ball, (i * texture_size, j * texture_size))
            else:
                screen.blit(window, (i * texture_size, j * texture_size)) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() 
    
    create_field(50)
    x, y = Hero.moving_hero(Hero.x, Hero.y, 50)
    screen.blit(hero, Hero.moving_hero(Hero.x, Hero.y, 50))
    pygame.display.flip()
    
   


