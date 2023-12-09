'''
Problem: Number Guessing Game

Create a simple number guessing game. In this game, a random number is generated 
and the player has to guess the number. The game provides feedback on whether 
the guess is too high or too low, and counts the number of tries taken to guess correctly.

Returns:
str: A message indicating the outcome of the game and the number of tries.
'''

import random

def check_number(secret_number, guess):
    
    if guess < secret_number:
        return "Too low!"
    elif guess > secret_number:
        return "Too high!"

    return True


print("Try to guess the secret number!")
print("Hint! The number is integer and within the range [1, 10] \n")

secret_number = random.randint(1, 10)
guess_attempts = 5

for attempt in range(guess_attempts):
    guess = int(input(f"This is your attempt {attempt + 1}/{guess_attempts}, what's your guess?"))
    result = check_number(secret_number, guess)
    if result is True:
        print(f"You got it! And it only took you {attempt + 1} tries!")
        exit()
    print(f"{result} \n")

print(f"Game over. The number was {secret_number}")

