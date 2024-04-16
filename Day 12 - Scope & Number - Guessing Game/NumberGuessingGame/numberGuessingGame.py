"""
NUMBER GUESSING GAME:
"""
import random
import os
import platform
from art import logo


def clear_screen():
    if platform.system() == 'windows':
        os.system('cls')  # Clear screen For Windows systems
    else:
        os.system('clear')  # Clear screen for Linux/OS X systems


def game_play():
    print(logo)
    secret_number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 - 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 10 if difficulty == 'easy' else 5

    for guessesTaken in range(attempts):
        print(f"You have {attempts - guessesTaken} attempts remaining to guess a number")
        guess = int(input("Make a guess: "))
        if guess == secret_number:
            print(f"You have guessed the secret number '{secret_number}' in '{guessesTaken}' attempt(s)")
            break
        elif guess < secret_number:
            print("Too low. ")
        else:
            print("Too high. ")

        if guessesTaken < attempts - 1:
            print("Guess again. ")
        else:
            print(f"You've run out of guesses, you lose. The number was {secret_number}")


while input("\nDo you want to play the Number Guessing Game? Type 'y' or 'n': ") == "y":
    clear_screen()
    game_play()
