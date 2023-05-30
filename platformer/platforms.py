import pygame
from settings import *
import sprites
import math
import random



# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.movement_indicator = 0
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.radius = 2

    def update(self):
        # self.rect.move_ip(-5, 0)  # Auto-scroll the platforms
        self.movement_indicator += PLATFORM_SPEED
        angle = math.radians(self.movement_indicator)  # Convert frame count to radians
        x = self.rect.centerx  # Calculate x-coordinate
        y = self.radius * math.sin(angle) + self.rect.centery  # Calculate y-coordinate
        self.rect.center = (x, y)  # Update the sprite's position
        # Remove platforms that go off-screen
        if self.rect.right <= 0:
            self.kill()
            

            
