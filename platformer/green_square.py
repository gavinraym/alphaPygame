import pygame
from settings import *
import sprites

  # GreenSquare class
class GreenSquare(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.image.fill("green")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.move_ip(-5, 0)  # Auto-scroll the green squares

        # Check collision with player
        if pygame.sprite.spritecollide(self, sprites.player, False):
            ADD_POINTS(1)
            self.kill()
            print("Points:", POINTS)
