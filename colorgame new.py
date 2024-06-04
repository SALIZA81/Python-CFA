# RAINBOW GAME

import random
import time

def play_color_game():
    """Plays a color guessing game with the user."""

    # array
    rainbow = ["red","orange","yellow","green","blue","indigo","violet"]

    # Score
    score = 0

    print("WELCOME TO THE RAINBOW COLOR GUESSING GAME!")
    print("I will think of a color, and you have to guess it.")

    while True:
        target_color = random.choice(rainbow)
        guess_attempts = 3

        print("\nI'm thinking of a color...")
        time.sleep(1)

        while guess_attempts > 0:
            guess = input("What color is it? ").lower()
            guess_attempts -= 1

            if guess == target_color:
                print("You guessed it right! 🎉")
                score += 1
                break
            else:
                print("Nope, that's not it. You have {} attempts left.".format(guess_attempts))

        if guess_attempts == 0:
            print(f"Sorry, you ran out of guesses. The color was {target_color}.")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again != 'y':
            break

    print(f"\nGame Over! Your final score is {score}.")

if __name__ == "__main__":
    play_color_game()