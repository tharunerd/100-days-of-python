# hangman game
# 
import random
from stages import stages


# Word list for the game
word_list = ["python", "hangman", "challenge", "programming", "code"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = len(stages) - 1

display = ["_"] * word_length
guessed_letters = []

print("Welcome to Hangman!")

while True:
    print(stages[len(stages) - 1 - lives])
    print("Word: " + " ".join(display))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                display[idx] = guess
        if "_" not in display:
            print("Congratulations! You guessed the word:", chosen_word)
            break
    else:
        print(f"'{guess}' is not in the word.")
        lives -= 1
        if lives == 0:
            print(stages[len(stages) - 1])
            print("Game Over! The word was:", chosen_word)
            break
