import pygame
import sys

class MainMenu:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.welcome_msg = "Welcome! Press Spacebar to start the game."
        self.running = True
    
    def draw_text(self, text, x, y):
        surface = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(surface, (x, y))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.running = False

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            
            text_width, text_height = self.font.size(self.welcome_msg)
            x = (self.screen.get_width() // 2) - (text_width // 2)
            y = (self.screen.get_height() // 2) - (text_height // 2)
            self.draw_text(self.welcome_msg, x, y)

            self.handle_events()

            pygame.display.flip()