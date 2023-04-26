## Brick Breaker

### This is a started project to help you learn how to code using ChatGPT and CoPilot. There are sections of this program that have not been written yet. It is up to you to decide what will happen, and you can use ChatGPT to figure out how to code it!

**Objectives:**

- Make the ball bounce off of the left wall. (ball.38)
- Prevent the paddle from going off screen. (paddle.17)
- Delete bricks when they are hit. (bricks.26)
- Display an ending message when ball goes off bottom of screen. (main.78)
- Add a score that is increased when bricks are hit. (brick.36)
- Whatever else you want to add!

Each of these objectives are available for you to work on in any order. Througout the code base, you will find '''comments''' with hints about what you can ask ChatGPT in order to learn more about the code and solve the objectives. Make sure and record the best prompts/responses from your convos in the log.txt file for later reference. 

### Before you begin...

It will be very helpful for you to know a little bit about Python and Pygame before you start this project. Here is a list of prompts that you can use to get a broad view of these tools. If you already know about some of these topics, you can skip them. 

- What is Python?
- What is Pygame?
- What is a main loop?
- What is a Pygame window, and how is it used?
- Why does a pygame window need to be cleared each frame, and how do I do that?
- What is a Pygame rect object? How do I draw one on a window, move it around, change its color, detect its collisions with other rects, and delete it?
- How are key presses handled in Pygame?
- What are events? And how does Pygame know when I close the game window?

### Setting up a new conversation...

ChatGPT will use information that you provided it previously in your conversation when generating responses. That means if you spend some time telling ChatGPT about your project first, it will be better able to answer your questions in a way that relates to your project. So, here are a few prompts about this project that you can use to get ChatGPT ready. Just open a new conversation, and copy-paste these prompts. Over time you can add more prompts about the project, or focus the prompts on specific areas of interest!

- I am working on a Python Pygame application. It is a simple brick breaker game, with a paddle at the bottom, bricks at the top, and a ball that bounces between them. 
- It contains 5 files: main.py (main loop and key inputs), ball.py (creating and moving a ball), bricks.py (creating and destroying bricks), paddle.py (creating and moving a paddle), and state.py (Contains variable references). 
- All the game objects are stored on state. The main loop calls state.BALL.move_ball() every frame. It calls state.PADDLE.move_paddle(x,y) only when the left and right keys are pressed. 
- When the ball needs to check for collisions with bricks, ball.py uses for row in state.BRICKS: for brick in row:
- Explain my program to me in simple terms.

After running these prompts, ChatGPT will be better able to give you specific code examples to add to your program. Just make sure if you create a new conversation, start again by giving some context about what you are working on!