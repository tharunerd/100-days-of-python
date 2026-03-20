# Day 12: Number Guessing Game

*100 Days of Code (Python Bootcamp Inspired by Dr. Angela Yu)*

## 🎯 Project Overview

Day 12 introduces a fun and interactive **Number Guessing Game**, where the player must guess a randomly generated number within a limited number of attempts.  
This project reinforces your understanding of **functions**, **conditionals**, **loops**, and **game logic**.

***

## 🧠 Concepts Covered

*   Importing and using the **random** module
*   Writing and organizing **functions**
*   Using **variables**, **loops**, and **conditionals**
*   Handling **user input**
*   Implementing **difficulty levels**
*   Creating a simple, interactive game flow

***

## 📝 Project Description

The goal of this project is to create a game where:

*   The program picks a random number between 1 and 100.
*   The player chooses a difficulty level (easy or hard).
*   Based on difficulty, the player gets a set number of attempts.
*   After each guess, the game provides feedback:
    *   “Too high!”
    *   “Too low!”
    *   “Correct!”
*   The game continues until the player wins or runs out of attempts.

You’ll also learn to structure your logic into reusable **functions** to keep your code clean and organized.

***

## 💡 Key Features

*   **Difficulty selection** (e.g., Easy = 10 attempts, Hard = 5 attempts)
*   **Clear feedback system** guiding the player after every guess
*   **Random number generation** for dynamic gameplay
*   **Looping structure** to handle multiple guesses
*   **Win/Lose conditions** based on remaining attempts

***

## 🛠️ Example Snippets

### 1) Random Number Generation

```python
import random
random_number = random.randint(1, 100)
```

### 2) Difficulty Setup

```python
def set_difficulty(level):
    return 10 if level == "easy" else 5
```

### 3) Guess Checking Logic

```python
def check_answer(guess, correct_number):
    if guess > correct_number:
        return "Too high!"
    elif guess < correct_number:
        return "Too low!"
    else:
        return "Correct!"
```

***

## 🔁 Game Flow Overview

1.  Display the welcome message
2.  Choose difficulty
3.  Generate a random number
4.  Loop through guesses:
    *   Player enters a guess
    *   Feedback provided
    *   Attempts decrease
    *   Check for win/loss
5.  End game message

***

## 🧪 Try-It-Yourself Ideas

*   Add a **replay option** to restart the game without exiting
*   Show a **history of guesses**
*   Add input validation for wrong inputs
*   Create a “hot/cold” feedback system based on distance from the target number

***

## 🗂️ Suggested Repo Structure

    📦 Day12-NumberGuessingGame
     ┣ 📄 number_guessing_game.py
     ┣ 📄 README.md
     ┗ 📄 logo.py

***

## ✨ Summary

By the end of Day 12, you will understand:

*   How to work with **functions** to structure game logic
*   How to use **loops and conditionals** effectively
*   How to create interactive, user-friendly programs
*   How to use **randomness** to make programs dynamic

