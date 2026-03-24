import turtle

# Create turtle object and screen
tim = turtle.Turtle()
screen = turtle.Screen()

# Movement functions
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_right():
    tim.setheading(tim.heading() - 10)

def turn_left():
    tim.setheading(tim.heading() + 10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# Key bindings
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear_screen, "c")

# Exit on click
screen.exitonclick()