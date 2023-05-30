import pygame
import sys
from settings import *

class EndScreen:
    def __init__(self):
        self.text = FONT.render(FAREWELL, True, (255, 255, 255))

    def draw(self, window):
        window.fill((0, 0, 0))  # Black background
        text_width, text_height = FONT.size(FAREWELL)
        x = (window.get_width() // 2) - (text_width // 2)
        y = (window.get_height() // 2) - (text_height // 2)
        window.blit(self.text, (x, y))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CHANGE_STATE(False)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    CHANGE_STATE("restart")

        return False
    
    def update(self, window):
        self.draw(window)
        self.handle_events()
        