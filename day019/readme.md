# 🐢 Day 19 –  Turtle Racing Game

### Turtle Movement, Screen Functions & Turtle Racing Project

Welcome to **Day 19** of the **100 Days of Python** journey!  
Today’s focus is on the **Turtle Graphics module**, one of the most fun ways to understand event-driven programming, movement systems, and screen-based interactions in Python.

***

## 📌 What You Learn in Day 19

### 🐢 What is the Turtle Module?

The `turtle` module lets you control a virtual “turtle” that moves around a window, drawing lines based on your commands.  
It is extremely useful for understanding:

*   Functions
*   Events & key listeners
*   Object-oriented programming
*   Animation basics
*   GUI interaction

***

## 🎮 Turtle Movement Methods

### **1. Forward & Backward**

Used to move the turtle along its current heading.

```python
tim.forward(10)
tim.backward(10)
```

### **2. Turning / Rotating**

Changes the turtle’s direction without moving it.

```python
tim.left(10)     # rotate left by 10 degrees
tim.right(10)    # rotate right by 10 degrees
```

You can also manually set an absolute direction:

```python
tim.setheading(90)  # 90° = Up
```

### **3. Pen Control**

Useful for drawing & clearing.

```python
tim.penup()
tim.pendown()
tim.clear()
```

### **4. Resetting Turtle Position**

Moves the turtle back to the center.

```python
tim.home()
```

***

## 🖥️ Screen Functions

The `Screen` object manages events, keyboard input, and window control.

### **1. Listening for Key Presses**

```python
screen.listen()
```

Enables event listening.

### **2. Binding Keys to Functions**

```python
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
```

This allows **real-time control**, like a mini drawing game.

### **3. Exiting the Window**

```python
screen.exitonclick()
```

Prevents the window from closing immediately.

***

# 🏁 Final Project – Turtle Racing Game

The highlight of Day 19 is the **Turtle Racing Game**, where multiple turtles race from the left side to the right.  
It introduces you to:

*   Random number generation
*   Looping animations
*   Creating multiple turtle objects
*   Handling user input (your bet)
*   Detecting a winner

### 🕹️ Game Flow

1.  The screen sets up a racetrack.
2.  You choose which turtle color you think will win.
3.  Each turtle moves forward by a random distance inside a loop.
4.  First turtle to cross the finish line wins.
5.  The game announces whether your bet was correct.

### 🎨 Concepts Used

*   `turtle.Turtle()` object creation
*   Lists for managing multiple turtles
*   `random.randint()`
*   Loops for animation
*   Text input with `screen.textinput()`

This project gives you the **first real experience of building a small interactive game** with Python.

***

## ✅ Summary

Day 19 teaches you the foundation of:

*   Moving objects on screen
*   Handling keyboard input
*   Using the screen as a GUI
*   Organizing functions
*   Building an event-driven game
*   Understanding object movement logic

And with all these concepts combined, you create a fun **Turtle Racing Game** at the end!

