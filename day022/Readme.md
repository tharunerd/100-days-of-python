# 🏓  Python Ping Pong Game

### *Day 22 — 100 Days of Python Bootcamp*

Inspired by the classic retro Pong arcade game, Day 22 was all about recreating a fully playable **two‑player Ping Pong game** using **Python** and the **Turtle Graphics** module.  
This project helped reinforce **Object‑Oriented Programming**, animation logic, collision detection, and event‑driven programming.

***

## 🌟 Features Overview

*   🏓 **Two-player paddle controls**
*   🔴 **Animated bouncing ball**
*   🎯 **Accurate collision detection**
*   🧮 **Scoreboard for both players**
*   ♻️ **Reset logic when a player misses**
*   ⚡ **Smooth, fluid gameplay using `tracer(0)`**

Perfect mix of fun + Python learning. 😄

***

# ✅ Features and Tasks Breakdown

## 1. 🎮 Game Window Setup

*   Created an **800×600** game window using `turtle.Screen()`
*   Customized background color and window title
*   Used `screen.tracer(0)` to disable auto-refresh
*   Manually updated screen each frame for smoother gameplay

***

## 2. 🏓 Paddle Creation (OOP)

Built a reusable **`Paddle` class** that:

*   Inherits from `turtle.Turtle`
*   Creates long rectangular paddles
*   Positions left and right paddles correctly
*   Includes methods:
    *   `go_up()`
    *   `go_down()`

This makes the paddles clean, modular, and easy to manage.

***

## 3. ⌨️ Paddle Controls

Assigned keyboard controls using:

```python
screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")
```

### Controls:

*   **Right Paddle** → ⬆ Up, ⬇ Down
*   **Left Paddle** → **W**, **S**

***

## 4. 🔴 Ball Creation & Movement

Created a **`Ball` class** with attributes for movement speed and direction.

### Ball Capabilities:

*   Moves diagonally using `.move()`
*   Bounces off top/bottom using `.bounce_y()`
*   Reverses X direction using `.bounce_x()`
*   Resets to center with `.reset_position()`

Movement speed increases after each paddle hit → makes the game more intense!

***

## 5. 💥 Collision Detection

*   Detected collision between **ball** and **paddles** using distance checks
*   Added conditions to ensure ball bounces only on correct side
*   Implemented wall detection:
    *   Bounces off top & bottom
    *   Triggers score update if ball goes past a paddle

Collision logic makes the game feel fast and responsive.

***

## 6. 🧠 Scoreboard System

A separate **`Scoreboard` class** displays player scores at the top.

### Scoreboard Features:

*   Tracks left and right player points
*   Updates automatically when a player scores
*   Centers all text using Turtle
*   Clean, simple UI with readable fonts

***

## 7. 🔁 Game Loop (Main Logic)

The heart of the game is a continuous loop that:

*   Updates the screen using `screen.update()`
*   Adds delay with `time.sleep()` for smooth animation
*   Moves the ball
*   Detects:
    *   Paddle collisions
    *   Wall collisions
    *   Misses (scoring events)
*   Updates scoreboard and resets ball when needed

This loop creates a simple but effective real-time game engine.

***

# 📁 Project File Structure

    day_022_ping_pong/
    │
    ├── main.py          # Game loop, collision logic, controls
    ├── paddle.py        # Paddle class (movement, position)
    ├── ball.py          # Ball class (movement, bouncing, speed)
    ├── scoreboard.py    # Scoreboard class (display & scoring)
    │
    └── README.md        # Project documentation

***

# 🕹️ Controls

### **Left Paddle**

*   **W** → Move Up
*   **S** → Move Down

### **Right Paddle**

*   **Up Arrow** → Move Up
*   **Down Arrow** → Move Down

***

# 🙌 Reflections

Day 22 was a perfect combination of fun and logic.  
Building Pong taught me how:

*   Game loops work
*   Objects interact in a game environment
*   Keyboard events are handled
*   Collision detection is implemented in real-time
*   OOP helps organize large programs into clean, reusable modules

This project massively improved my confidence in building interactive applications with Python.
