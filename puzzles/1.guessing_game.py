

""" BEGINNING PROMPT

Create a python application where the player tries to guess a randomly
generated number between 1 and 20 in 6 tries or less. The game should prompt
the player to guess, and provides feedback based on whether the guess is too 
high or too low. If the player guesses the number within 6 tries, 
they win the game. If they don't guess the number in time, the game reveals the 
number and the player loses.

   """

### ADD THE CODE GENERATED BY CHATGPT HERE ###
import random

def guess_number():
    # generate a random number between 1 and 20
    number = random.randint(1, 20)

    # give the player 6 chances to guess the number
    for i in range(6):
        guess = int(input("Guess the number between 1 and 20: "))
        if guess == number:
            print("Congratulations! You guessed the number.")
            return
        elif guess < number:
            print("The number is higher.")
        else:
            print("The number is lower.")
    print("Sorry, you didn't guess the number. The number was", number)

guess_number()


### Run your program and see if it works. Does it do what you expect?

### How might you change this game to make it more fun? Come up with some ideas
### and then write some prompts to get ChatGPT to make your ideas into code.

### Here are some example prompts that you can play around with.
### Add some of yours here too. Also record what each prompt added to
### your program. 

'''Add a scoring system. The fewer guesses the player uses, the more points 
they should get'''

'''Let the player continue playing as many times as they want without resetting
their score.'''

'''Add a rainbow colored title that displays before the game starts, and says
This is a guessing game!' Also tell the player the rules, and ask if they
are ready to play. Then clear the terminal and start the game. '''

    # ADD YOUR PROMPTS HERE