# 🐢 Day 18 – Turtle Graphics & Drawing Shapes

Welcome to **Day 18** of my **100 Days of Python Bootcamp** journey!  
Today, I explored the **Turtle graphics** library to draw shapes, understand RGB color modes, and build creative patterns using Python.

***

## 📘 **What I Learned**

### ✔ Introduction to Turtle Graphics

*   Understanding how the **Turtle** object works
*   Moving forward, backward, turning, changing pen size, and colors

### ✔ Drawing Geometric Shapes

*   Squares
*   Polygons
*   Dashed lines

### ✔ Playing with Colors

*   Using both named colors
*   Switching to **RGB color mode (0–255)** for custom colors

### ✔ Random Walks & Spirographs

*   Generating patterns using loops
*   Randomizing direction and color
*   Speeding up the turtle for smoother animations

***

## 🧪 **Key Concepts & Functions Used**

| Concept           | Function / Method                                 |
| ----------------- | ------------------------------------------------- |
| Moving the turtle | `forward()`, `backward()`, `left()`, `right()`    |
| Pen control       | `penup()`, `pendown()`, `pencolor()`, `pensize()` |
| Colors            | `color()`, `colormode(255)`                       |
| Speed             | `speed("fastest")`                                |
| Random            | `import random` for random colors/directions      |
| Screen setup      | `Screen()` for window control                     |

***

## 🖼 **Sample Code Snippet — Random Walk**

```python
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.pensize(10)

directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
```

***

## 🎯 **Project Output**

*   A colorful **random walk pattern**
*   Smooth, vibrant lines and turns using random RGB colors  
    (You can add screenshots of your output here.)

***

## 🚀 **Skills Gained**

*   Basic graphics programming
*   Understanding of loops and modular code
*   Working with RGB colors
*   Creative coding & pattern generation

***

## 📂 **Folder Structure**

    Day-18/
    │── main.py
    │── random_walk.py
    │── spirograph.py
    └── README.md

***
