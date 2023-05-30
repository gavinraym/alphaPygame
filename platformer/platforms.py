import pygame
from settings import *
import sprites
import math
import random


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
        self.radius = 2

    def update(self):
        # self.rect.move_ip(-5, 0)  # Auto-scroll the platforms
        global frame_count  # Declare frame_count as a global variable
        angle = math.radians(frame_count)  # Convert frame count to radians
        x = self.rect.centerx  # Calculate x-coordinate
        y = self.radius * math.sin(angle) + self.rect.centery  # Calculate y-coordinate
        self.rect.center = (x, y)  # Update the sprite's position
        # Remove platforms that go off-screen
        if self.rect.right <= 0:
            self.kill()
            
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
        # self.rect.move_ip(-5, 0)  # Auto-scroll the green squares

        # Check collision with player
        if pygame.sprite.spritecollide(self, sprites.player, False):
            ADD_POINTS(1)
            self.kill()
            print("Points:", POINTS)

            

def start():
    starting_platform = Platform(WINDOW_WIDTH // 2 + PLATFORM_WIDTH // 2, WINDOW_HEIGHT - PLATFORM_HEIGHT -50)
    sprites.platforms.add(starting_platform)
    create_platforms()

def create_platforms():
    random_height = random.randint(50, WINDOW_HEIGHT - PLATFORM_HEIGHT - 150)
    x = WINDOW_WIDTH # Starting x-coordinate for the first platform
    y = WINDOW_HEIGHT - PLATFORM_HEIGHT - random_height  # y-coordinate for all platforms

    platform = Platform(x, y)
    platforms.append(platform)
    sprites.platforms.add(platform)
 # Randomly create green squares
    if random.random() < 0.4:  # Adjust the probability as needed
        green_square = GreenSquare(x, y - SQUARE_SIZE)
        sprites.platforms.add(green_square)

def update():
    global frame_count  # Declare frame_count as a global variable
    frame_count += 1
    # Auto-scroll the platforms
    for platform in sprites.platforms.sprites():
        platform.rect.move_ip(-5, 0)
        
    # Indevidual platform update
    for platform in sprites.platforms:
        platform.update()
        
    if frame_count % 25 == 0:
        create_platforms()
