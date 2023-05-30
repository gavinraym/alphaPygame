# Initialize Pygame 
import pygame
import sys 
pygame.init()
pygame.font.init()

# Initializing window
from settings import *
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Auto-Scroller Platformer")
clock = pygame.time.Clock()

# Initialize modules
from main_menu import MainMenu
from game_loop import GameLoop
from game_over import EndScreen
main_menu = MainMenu()
game_loop = GameLoop()
end_screen = EndScreen()

state = True
# Run main loop
while state:
    state = GET_STATE()
    if state == "main_menu":
        # Show main menu
        main_menu.update(window)
        
    elif state == "start":
        # Start a new game
        game_loop.start()
        
    elif state == "running":
        # Run the game
        game_loop.update(window)
        
    elif state == "game_over":
        # Show game over screen
        end_screen.update(window)
        
    elif state == "restart":
        # Reset game-specific variables here, like score, etc.
        RESET_POINTS()
        # Change the state
        CHANGE_STATE("start")
        
    # Refresh the display
    pygame.display.flip()
    clock.tick(FPS)
        
# To quit the game, set STATE to False i.e. SET_STATE(False)
pygame.quit()    
sys.exit()  