import pygame
import state

# Create a full set of bricks
def create_bricks():
    """What is a Python for loop?"""
    """What is the Python range() function?"""
    for i in range(state.BRICK_ROWS):
        """What syntax is used for lists in Python?"""
        row = []
        for j in range(state.BRICK_COLS):
            # calculate the brick's position
            x = j * (state.BRICK_WIDTH + state.BRICK_SPACING) + state.BRICK_SPACING
            y = i * (state.BRICK_HEIGHT + state.BRICK_SPACING) + state.BRICK_SPACING + 50
            """What is a pygame rect object?"""
            rect = pygame.Rect(x, y, state.BRICK_WIDTH, state.BRICK_HEIGHT)
            row.append(rect)
        """What happens when you append a list to a list?"""
        state.BRICKS.append(row)
     
# Function to remove a brick from the game   
def destroy_brick(row, col):
    # row is the row of the brick to remove
    # col is the column of the brick to remove
    
    ### This is where you should remove the bricks from the game. ###
    """How do Python lists work?  What is an index?"""
    """How do you remove an item from a list?"""
    """What is a 2d list?  How do you access an item in a 2d list?"""
    """How do you remove an item from a 2d list givin the row and column?"""
    
    ### YOUR CODE GOES HERE ###
        
        
    
    ### This is also where you should add code to increase state.SCORE ###
    
    """What is the augmented assignment operator?"""
    """How do you increase a variable by 1?"""
    """How do you change a variable in a different file that is being imported?"""
    
    ### YOUR CODE GOES HERE ###