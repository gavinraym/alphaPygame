import pygame

# Constants
FPS = 40

# Game window dimensions
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 600

# Platform dimensions
PLATFORM_WIDTH = 125
PLATFORM_HEIGHT = 20
PLATFORM_FREQUENCY = 24
PLATFORM_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLUE = (100, 250, 155)
GREEN =(0,255,0)

FONT = pygame.font.Font(None, 32)

# Player dimensions and attributes
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
PLAYER_JUMP_HEIGHT = 25
PLAYER_GRAVITY = 1

POINTS=0
STATE="main_menu"

#Square settings
SQUARE_SIZE = 25
SQUARE_SIZE = 25

# Text settings
WELCOME = "Welcome! Press Spacebar to start the game."
FAREWELL = "Game Over! Press Spacebar to restart the game."

def CHANGE_STATE(value):
    print("changing state to: ", value)
    global STATE
    STATE = value
    
def GET_STATE():
    return STATE

def ADD_POINTS(value):
    global POINTS
    POINTS += value
    
def RESET_POINTS():
    global POINTS
    POINTS = 0
