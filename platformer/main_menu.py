import pygame
import sys
from settings import *

class MainMenu:
    def __init__(self):
        self.welcome_msg = FONT.render(
            WELCOME,
            True,
            (255, 255, 255))
    
    def draw_text(self, window):
        window.fill((0, 0, 0))  # Black background
        text_width, text_height = FONT.size(WELCOME)
        x = (window.get_width() // 2) - (text_width // 2)
        y = (window.get_height() // 2) - (text_height // 2)
        window.blit(self.welcome_msg, (x, y))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CHANGE_STATE(False)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    CHANGE_STATE("start")

    def update(self, window):
        self.draw_text(window)
        self.handle_events()

