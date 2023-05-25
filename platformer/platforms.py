import pygame
from settings import *
import sprites

platforms = []
frame_count = 0

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.move_ip(-5, 0)  # Auto-scroll the platforms

        # Remove platforms that go off-screen
        if self.rect.right <= 0:
            self.kill()

def start():
    starting_platform = Platform(WINDOW_WIDTH // 2 + PLATFORM_WIDTH // 2, WINDOW_HEIGHT - PLATFORM_HEIGHT)
    sprites.platforms.add(starting_platform)

def create_platforms():
    x = WINDOW_WIDTH + PLATFORM_WIDTH  # Starting x-coordinate for the first platform
    y = WINDOW_HEIGHT - PLATFORM_HEIGHT  # y-coordinate for all platforms

    platform = Platform(x, y)
    platforms.append(platform)
    sprites.platforms.add(platform)


def update():
    global frame_count  # Declare frame_count as a global variable
    frame_count += 1
    for platform in sprites.platforms:
        platform.update()
    if frame_count % 10 == 0:
        create_platforms()
