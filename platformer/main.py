from settings import *
import pygame
import sys
import player
import platforms
import sprites
from main_menu import MainMenu
from game_over import EndScreen

# Initialize Pygame     
pygame.init()

pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 32)

main_menu = MainMenu(screen, font)
main_menu.run()
end_screen = EndScreen(WINDOW_WIDTH , WINDOW_HEIGHT)

# Define states, Menu, Start, Game, GameOver
current_state = "Start"
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


    if GAME_OVER:
        # Game over state
        end_screen.draw()
        play_again = end_screen.handle_events()
        if play_again:
            # Reset the game state and variables
            CHANGE_STATE("GAME_OVER", False)
            # ... Reset game-specific variables here ...

    else:
    
        # Update
        player.update()
        platforms.update()

        # Draw
        window.fill((0, 0, 0))
        sprites.player.draw(window)
        sprites.platforms.draw(window)

        pygame.display.flip()
        clock.tick(40)






pygame.quit()