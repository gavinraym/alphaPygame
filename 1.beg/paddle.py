import pygame
import state


# create a paddle
def create_paddle():
    state.PADDLE = pygame.Rect(state.WINDOW_WIDTH // 2 - state.PADDLE_WIDTH // 2, state.WINDOW_HEIGHT - 50, state.PADDLE_WIDTH, state.PADDLE_HEIGHT)


# The following is a python function.
# For more information on functions, try asking ChatGPT, 
#   "What is a Python function?"
#   "Whait is an argument?"
#   "What is a return value?"
def move_paddle(x,y):
    
    ### This is where you should add code to stop the paddle from moving
    ### off the right edge of the screen.###
    """How can I detect if an object is touching the edge of the screen?"""
    """How can I use an if statement to stop some code from running?"""
    
    ### ADD YOUR CODE HERE ###
    
    
    

    ## This moves the paddle
    state.PADDLE.left += x
    state.PADDLE.top += y
    
       
# Create a new function that changes the paddle in a new way.
# You can ask ChatGPT, "How do I change the size of a pygame Rect?"
# Or come up with your own prompt/objective.
def my_paddle_change(arg):
    # Your code here
    print("My paddle change is called with the argument: " + str(arg))
    