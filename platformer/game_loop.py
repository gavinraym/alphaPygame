import pygame
from platforms import Platform
from player import Player
from green_square import GreenSquare
import sprites
from settings import *
import random

class GameLoop():
    def __init__(self):
        self.player = Player()
        self.frame_count = PLATFORM_FREQUENCY

    def start(self):
        # Erase all current sprites
        sprites.platforms.empty()
        sprites.platforms.add(Platform(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 150))
        sprites.player.empty()
        self.player = Player()
        sprites.player.add(self.player)
        sprites.green_squares.empty()
        self.create_platforms()
        CHANGE_STATE("running")

    def create_platforms(self):
        random_height = random.randint(50, WINDOW_HEIGHT - PLATFORM_HEIGHT - 150)
        x = WINDOW_WIDTH # Starting x-coordinate for the first platform
        y = WINDOW_HEIGHT - PLATFORM_HEIGHT - random_height  # y-coordinate for all platforms

        platform = Platform(x, y)
        sprites.platforms.add(platform)
        
    # Randomly create green squares
        if random.random() < 0.8:  # Adjust the probability as needed
            green_square = GreenSquare(x, y - SQUARE_SIZE)
            sprites.green_squares.add(green_square)

    def update(self, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CHANGE_STATE(False) 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                    
                    
        # Auto-scroll the platforms and green squares
        for platform in sprites.platforms.sprites():
            platform.rect.move_ip(-5, 0)
        for green_square in sprites.green_squares.sprites():
            green_square.rect.move_ip(-5, 0)
            
        # Individual platform update
        for platform in sprites.platforms:
            platform.update()
            
        # Green square update
        for green_square in sprites.green_squares:
            green_square.update()
            
        # Create new platforms
        self.frame_count -= 1    
        if self.frame_count == 0:
            self.create_platforms()
            self.frame_count = PLATFORM_FREQUENCY
            
        # Update
        self.player.update()

        # Draw
        window.fill((0, 0, 0))
        sprites.player.draw(window)
        sprites.platforms.draw(window)
        sprites.green_squares.draw(window)
        
   
        
        
    
