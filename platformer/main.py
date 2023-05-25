from settings import *
import pygame
import sys
import player
import platforms
import sprites

# Initialize Pygame
pygame.init()

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Auto-Scroller Platformer")
clock = pygame.time.Clock()

def game_over():
    pygame.quit()
    sys.exit()

player.start()
platforms.start()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Update
    player.update()
    platforms.update()

    # Draw
    window.fill((0, 0, 0))
    sprites.player.draw(window)
    sprites.platforms.draw(window)

    pygame.display.flip()
    clock.tick(40)

# Quit the game
pygame.quit()
