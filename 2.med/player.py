import pygame
import os
from pygame.locals import *
import STATE
import sys

image = pygame.image.load(os.path.join('assets','hero1.png'))
image = pygame.transform.scale(image, (32, 32))
x = 0
y = 0

def take_turn():
    global x, y
    
    # check for key presses
    # This is where we determine what the player does
    # when keys are pressed.
    
    # For more information, try asking ChatGPT the following:
    # "What is the pygame event queue?"
    # "What is the pygame event type?"
    # "What is the pygame event key?"
    # "How do I make a sprite move faster when shift is pressed down?"
 
    for event in pygame.event.get():
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x -= 5
                elif event.key == K_RIGHT:
                    x += 5
                elif event.key == K_UP:
                    y -= 5
                elif event.key == K_DOWN:
                    y += 5
                
    STATE.SCREEN.blit(image, (x, y))