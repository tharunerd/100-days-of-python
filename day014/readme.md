# Day 14: Higher–Lower Game

*100 Days of Code (Python Bootcamp Inspired by Dr. Angela Yu)*

## 🎯 Project Overview

Day 14 focuses on building the **Higher–Lower Game**, a fun comparison-based guessing game where the player must choose which of two options has a higher numerical value (usually follower counts, scores, or any comparable metric).  
This project reinforces your understanding of **functions**, **loops**, **game flow**, and **data handling**.

***

## 🧠 Concepts Covered

*   Working with **dictionaries** and **lists of data**
*   Importing data from external files (e.g., a list of celebrities or accounts)
*   Writing **reusable functions**
*   Handling **game logic** and **score tracking**
*   Using **clear and modular code structure**
*   Control flow with **while loops**, **if/else**, and comparing values

***

## 📝 Project Description

Your task is to build a simple game where:

*   Two random entries (A and B) are shown to the player.
*   Each entry contains descriptive info (e.g., name, profession, country) and a numeric value (e.g., follower count).
*   The player must guess **which one has the higher number**.
*   If the player is correct → score increases and the game continues.
*   If the player is wrong → the game ends and the final score is displayed.

As the player continues, one of the options carries over to the next round, making the game more challenging and dynamic.

***

## 💡 Key Features

*   **Random data selection** to keep gameplay fresh
*   **Comparison function** to determine the correct answer
*   **Score tracking** that updates each round
*   **Game loops** to allow multiple rounds until the player guesses wrong
*   **Clean UI** using prints and formatted output
*   A clear, modular structure for readability and future expansion

***

## 🛠️ Example Snippets

### 1) Picking Random Data

```python
import random

choice_a = random.choice(data)
choice_b = random.choice(data)
```

### 2) Comparing Values

```python
def check_answer(guess, a_value, b_value):
    if a_value > b_value:
        return guess == "a"
    else:
        return guess == "b"
```

### 3) Basic Game Loop

```python
game_active = True
score = 0

while game_active:
    # show choices
    # take input
    # check answer
    # update score or end game
    pass
```

***

## 🔁 Game Flow Overview

1.  Display the game logo (optional)
2.  Randomly select two data entries
3.  Show their descriptions (but hide their values)
4.  Ask the player: **Who has more? “A” or “B”?**
5.  Compare values and determine correctness
6.  If the player is right → score + 1, continue with new data
7.  If wrong → display final score and end the game

***

## 🧪 Try-It-Yourself Ideas

*   Add **difficulty levels** (e.g., faster rounds or trickier comparisons)
*   Add **categories** the player can choose from
*   Track **high scores** across sessions
*   Add **ASCII art** for the intro and transitions
*   Create a “best-of-5” challenge mode

## ✨ Summary

By the end of Day 14, you will understand:

*   How to use functions to organize complex game logic
*   How to work with lists, dictionaries, and random selections
*   How to use loops and conditionals to create interactive games
*   How to build a smooth, replayable user experience

This day marks the end of the **Beginner** section of the 100 Days of Python and prepares you for more structured, intermediate-level challenges.

***
