# 🐍 Python Snake Game

### *Day 20 & Day 21 — 100 Days of Python Bootcamp*

Recreating the **iconic Nokia Snake game** was easily one of the most nostalgic and enjoyable parts of my Python journey.  
Using **Object-Oriented Programming (OOP)** and the **Turtle Graphics** module, I built a fully functional Snake Game with smooth movement, collision detection, and a modular file structure.

***

## 🎮 Game Preview

✔ Smooth movement  
✔ Responsive controls  
✔ Food spawning  
✔ Visible boundaries  
✔ Scoreboard  
✔ Clean OOP architecture

> *A simple, fun, and powerful beginner-friendly project that teaches real game logic!*

***

## 🚀 Features

*   🐍 **Classic Snake gameplay**
*   🎯 **Wall, food, and tail collision detection**
*   ⚡ **Smooth continuous movement**
*   🍏 **Random food generation**
*   ➕ **Snake grows after eating**
*   🎁 **Dynamic scoreboard**
*   🧩 **OOP‑based modular structure**

***

## 🧠 Concepts Applied

This project helped me deeply understand:

### **✔ Object-Oriented Programming**

*   Classes, objects, attributes
*   Encapsulation & modular design
*   Reusability of methods

### **✔ Game Development Logic**

*   Movement loops
*   Frame refresh using `screen.tracer(0)`
*   Collision detection math
*   Boundary restrictions

### **✔ Event-Driven Programming**

*   Keyboard input handling
*   Constant screen updates
*   Listening for user actions

### **✔ Turtle Module Usage**

*   Turtle shapes, colors, movement
*   Creating custom objects
*   Controlling the screen

***

# 📁 Project File Structure

    day_020_021_snake_game/
    │
    ├── main.py          # Game loop, event listeners, collision logic
    ├── snake.py         # Snake class: movement, growth, reset
    ├── food.py          # Food class: random placement
    ├── score.py         # Scoreboard class: display & updates
    │
    └── README.md        # Project documentation (this file)

***

# 🔍 Methods & Classes Breakdown

## 🐍 **Snake Class (snake.py)**

Handles everything related to the snake’s body and movement.

### **Key Methods**

| Method                                | Purpose                          |
| ------------------------------------- | -------------------------------- |
| `move()`                              | Moves the snake forward smoothly |
| `extend_segment()`                    | Adds a new segment after eating  |
| `up()`, `down()`, `left()`, `right()` | Direction controls               |
| `reset()`                             | Resets the snake after death     |
| `create_snake()`                      | Initializes starting snake body  |

***

## 🍏 **Food Class (food.py)**

Handles food appearance and random repositioning.

### **Key Methods**

| Method       | Purpose                                 |
| ------------ | --------------------------------------- |
| `refresh()`  | Places food at a random (x, y) position |
| `__init__()` | Sets shape, color, and initial position |

***

## 🧾 **Scoreboard Class (score.py)**

Displays the player's score on screen.

### **Key Methods**

| Method             | Purpose                              |
| ------------------ | ------------------------------------ |
| `increase_score()` | Adds +1 when snake eats food         |
| `update_score()`   | Refreshes score text                 |
| `game_over()`      | Displays GAME OVER message at center |

***

# 🚦 Controls

| Key           | Action     |
| ------------- | ---------- |
| ⬆ Up Arrow    | Move Up    |
| ⬇ Down Arrow  | Move Down  |
| ⬅ Left Arrow  | Turn Left  |
| ➡ Right Arrow | Turn Right |

Simple and intuitive — just like the original game.

***

# 🛠️ How to Run the Game

### **1. Clone the Repository**

```bash
git clone https://github.com/tharunerd/one-hundred-days-of-python.git
cd day_020,021
```

### **2. Run the Game**

```bash
python main.py
```

Python's `turtle` module comes built-in — no extra installation needed!

***

# 🙌 Reflections

Rebuilding this childhood classic brought back a lot of memories from the Nokia era.  
But more importantly, I learned:

*   How game loops actually function
*   How to structure projects using OOP
*   How event-driven systems work
*   How to organize files for readability
*   How to think logically for collision & movement

This project was **fun, nostalgic, and a huge confidence booster** in Python.

