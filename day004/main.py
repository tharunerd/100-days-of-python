# rock paper scissors game
# understanding random module in python
# This code implements a simple rock-paper-scissors game where the player can choose rock, paper


import random

players_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
choices = ["rock", "paper", "scissors"]
if players_choice not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
else:
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if players_choice == computer_choice:
        print("It's a tie!")
    elif (players_choice == "rock" and computer_choice == "scissors") or \
         (players_choice == "paper" and computer_choice == "rock") or \
         (players_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")