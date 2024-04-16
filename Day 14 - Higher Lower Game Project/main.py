"""
A HIGHER OR LOWER COMPARISON GAME
"""

import os
import random
from art import logo, vs
from game_data import data


def clear_screen():
    """Function to help clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_random_profile(exclude=None):
    """Select and return a random profile from the global 'data' list of profiles."""
    if exclude is not None:
        available_data = [profile for profile in data if profile != exclude]
    else:
        available_data = data
    return random.choice(available_data)


def play_game():
    score = 0
    playing = True
    first_guess = True  # Flag to control the score display
    profile_a = get_random_profile()

    while playing:
        clear_screen()
        print(logo)

        if not first_guess:  # Check if it's not the first guess anymore
            print(f"You're right! Current score: {score}")

        profile_b = get_random_profile(exclude=profile_a)

        print(f"\nCompare A: {profile_a['name']}, a {profile_a['description']} from {profile_a['country']}.")
        print(vs)
        print(f"Against B: {profile_b['name']}, a {profile_b['description']} from {profile_b['country']}.")

        guess = input("\nWhich profile has more followers? Type 'A' or 'B': ").strip().upper()

        if profile_a['follower_count'] > profile_b['follower_count']:
            correct_answer = 'A'
        else:
            correct_answer = 'B'

        if guess == correct_answer:
            score += 1
            # print(f"You're right! Current score: {score}")
            profile_a = profile_b  # if guess == 'A' else profile_b
            first_guess = False  # Update a flag after the first correct guess
        else:
            clear_screen()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            playing = False

        if not playing:
            play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if play_again == 'yes':
                playing = True
                profile_a = get_random_profile()
                score = 0
                first_guess = True  # Reset this for the new game
            else:
                print("\nThanks for playing!!!")


def main():
    print("Welcome to the Higher Lower Game!")
    play_game()


if __name__ == "__main__":
    main()
