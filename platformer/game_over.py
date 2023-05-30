import pygame
import sys

class EndScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.Font(None, 36)
        self.text = "Game Over"
        self.text_rect = None
        self.button = pygame.Rect(width // 2 - 50, height // 2 + 50, 100, 50)
        self.button_text = "Play Again"
        self.button_text_rect = None

    def draw(self):
        self.screen.fill((0, 0, 0))  # Black background

        # Draw the game over text
        self.text_rect = self.font.render(self.text, True, (255, 255, 255)).get_rect(center=(self.width // 2, self.height // 2 - 50))
        self.screen.blit(self.font.render(self.text, True, (255, 255, 255)), self.text_rect)

        # Draw the play again button
        pygame.draw.rect(self.screen, (0, 255, 0), self.button)
        self.button_text_rect = self.font.render(self.button_text, True, (0, 0, 0)).get_rect(center=self.button.center)
        self.screen.blit(self.font.render(self.button_text, True, (0, 0, 0)), self.button_text_rect)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.button.collidepoint(mouse_pos):
                    # Play again button clicked
                    return True

        return False