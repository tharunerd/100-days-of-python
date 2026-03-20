import random
from logo import logo


EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def check_guess(guess, answer):
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low.")
        return False
    else:
        print(f"You got it! The answer was {answer}.")
        return True

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    attempts = set_difficulty()
    guessed = False

    while attempts > 0 and not guessed:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        guessed = check_guess(guess, answer)
        if not guessed:
            attempts -= 1
            if attempts > 0:
                print("Guess again.")
            else:
                print(f"You've run out of guesses. The answer was {answer}.")

if __name__ == "__main__":
    game()


# This code implements a number guessing game where the player has to guess a randomly generated number between 1 and 100.
# The player can choose between easy and hard difficulty levels, which determine the number of attempts allowed
