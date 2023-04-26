import pygame
import state
import bricks


# Create a ball object
def create_ball():
    """where would window width devided by 2 minus object width devided by 2 be?"""
    state.BALL = pygame.Rect(state.WINDOW_WIDTH // 2 - state.BALL_WIDTH // 2, state.WINDOW_HEIGHT - 70, state.BALL_WIDTH, state.BALL_HEIGHT)
    
def move_ball():
    # move the ball
    """What is the rect.left attribute?"""
    state.BALL.left += state.BALL_SPEED_X
    state.BALL.top += state.BALL_SPEED_Y
    
    # check for collisions with paddle
    """What is the rect.colliderect() method?"""
    if state.BALL.colliderect(state.PADDLE):
        state.BALL.top = state.PADDLE.top - state.BALL_HEIGHT
        state.BALL_SPEED_Y = -state.BALL_SPEED_Y
        
    # Check for collisions with bricks
    """How can I iterate over a lists indexes?"""
    for row in range(len(state.BRICKS)):
        """How can I iterate over a 2d lists indexes, as row and col?"""
        for col in range(len(state.BRICKS[row])):
            if state.BALL.colliderect(state.BRICKS[row][col]):
                bricks.destroy_brick(row, col)
                state.BALL_SPEED_Y = -state.BALL_SPEED_Y
                break

   # check for ball hitting the edges of the screen
    """What is a comparison operator?  What does it return?"""
    if state.BALL.right >= state.WINDOW_WIDTH:
        state.BALL_SPEED_X = -state.BALL_SPEED_X
        
        ### This is where you should add code to make the ball
        # bounce off the left wall .###
        """How would I check if a rect is touching the edge of the screen?"""
        """How do I reverse its direction if I have a state.BALL_SPEED_X variable?"""
        ### ADD YOUR CODE HERE ###
        
        
        
    if state.BALL.top <= 0:
        state.BALL_SPEED_Y = -state.BALL_SPEED_Y
  
    ### This is where you should add code to set state.GAME_OVER to True
    ### when the ball leaves the bottom of the screen. ###
    
    """How do I check if a rect is touching the bottom of the screen?"""
    """How do I set a variable to False in a file that is being imported?"""
    """What is a global static variable?"""
    ## ADD YOUR CODE HERE ###