import pygame
import state

# initialize Pygame
"""What does Pygame.init() do?"""
pygame.init()

# create a game window
"""What is a game window? And what does pygame.display.set_mode() do?"""
state.WINDOW = pygame.display.set_mode((state.WINDOW_WIDTH, state.WINDOW_HEIGHT))

# set up the game clock
"""Why does Pygame need a clock? How is it used? What are fps?"""
state.CLOCK = pygame.time.Clock()


# Import game modules and create game objects
"""In Python, how are modules imported?"""
"""In Python, how do I call a function from an imported module?"""
# create bricks
import bricks
bricks.create_bricks()
# create a ball
import ball
ball.create_ball()
# create a paddle
import paddle
paddle.create_paddle()



# set up the game loop
"""What is the Pygame game loop?"""
"""What is a Pythan while loop?"""
while not state.GAME_OVER:
    
    # handle events
    """What are Pygame events? And how are they retrieved?"""
    for event in pygame.event.get():
        """What triggers the pygame.QUIT event?"""
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # move the paddle
    """What does pygame.key.get_pressed() do?"""
    """What are Pygame key events? pygame.K_LEFT? pygame.K_RIGHT?"""
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_paddle( -state.PADDLE_SPEED, 0)   
    if keys[pygame.K_RIGHT]:
        paddle.move_paddle( state.PADDLE_SPEED, 0)
        
    # move the ball
    ball.move_ball()

    # draw the game objects
    """Why do I need to fill the window each frame?"""
    """Are are the three arguments used by draw.rect()?"""
    state.WINDOW.fill((0, 0, 0))
    pygame.draw.rect(state.WINDOW, (255, 255, 255), state.PADDLE)
    pygame.draw.rect(state.WINDOW, (255, 255, 255), state.BALL)
    
    # draw the bricks
    """What is a Python for loop?"""
    """How are 3d arrays represented in Python? How would I for loop over each element?"""
    for row in state.BRICKS:
        for brick in row:
            pygame.draw.rect(state.WINDOW, (255, 255, 255), brick)
            
    """What is pygame.display.update()?"""
    pygame.display.update()

    # limit the frame rate
    """What is a good frame rate, and why should I limit it?"""
    state.CLOCK.tick(60)

### This is where you should add code to display a game over message.###
"""Can I start a new while loop after the game is over to display a game over message?"""
"""How do I display text in Pygame?"""
"""How do I display the player's state.SCORE in the center of the screen?"""

### ADD YOUR CODE HERE ###




# quit Pygame
"""What happens when pygame.quit() is called?"""
pygame.quit()
