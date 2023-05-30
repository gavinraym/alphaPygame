# Constants
FPS = 60

# Game window dimensions
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 600

# Platform dimensions
PLATFORM_WIDTH = 125
PLATFORM_HEIGHT = 20

# Colors
WHITE = (255, 255, 255)
BLUE = (100, 250, 155)

# Player dimensions and attributes
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 40
PLAYER_JUMP_HEIGHT = 25
PLAYER_GRAVITY = 1

POINTS=0
# Game states
GAME_OVER = False

#Square settings
SQUARE_SIZE = 25
SQUARE_SIZE = 25

def CHANGE_STATE(state, value):
    if state == "GAME_OVER":
        GAME_OVER = value

def ADD_POINTS(value):
    POINTS += value
#