import pygame
from pygame.locals import *
import sys
import STATE
import player


STATE.SCREEN = pygame.display.set_mode((STATE.WIDTH, STATE.HEIGHT))

while True:
    
    

    # update the player here
    player.take_turn()

    # draw the game graphics here

    pygame.display.update()
