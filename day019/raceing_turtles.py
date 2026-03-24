# import turtle
# import random
#
# race_onn =  False
# screen = turtle.Screen()
# screen.setup(width=666, height=444)
# user_guess = screen.textinput(title= "make you bet on a colored turtle: red, blue, yellow, orange, pink, green , brown" , prompt= "entre a colour :")
# y_positions = [150, 90, 30,  -30, -90, -150 ]
# color = ["red", "blue", "yellow", "orange", "pink", "green" , 'brown']
# all_turtles = []
#
# for turtle_index in range (0, 6):
#     tim = turtle.Turtle(shape="turtle")
#     tim.color(color[turtle_index])
#     tim.penup()
#     tim.goto(x= -250 , y= y_positions[turtle_index])
#     all_turtles.append(tim)
#     tim.speed(1000)
# if user_guess:
#     race_onn = True
#
# while race_onn:
#
#     for turtle in all_turtles:
#         if turtle.xcor() > 245 :
#             race_onn = False
#             winning_turtle = turtle.pencolor()
#             if winning_turtle == user_guess:
#                 print(f"you guess right {winning_turtle}, is the winner")
#             else:
#                 print(f"your guess is wrong {winning_turtle} is the winner")
#
#
#         random_distance = random.randint(0,10)
#         turtle.forward(random_distance)
#
# screen.exitonclick()
#
import turtle
import random

race_onn = False
screen = turtle.Screen()
screen.setup(width=666, height=444)

# List of valid colors
colors = ["red", "blue", "yellow", "orange", "pink", "green"]
y_positions = [150, 90, 30, -30, -90, -150]
all_turtles = []

# Get user input
user_guess = screen.textinput(
    title="Make your bet!",
    prompt="Enter a color: red, blue, yellow, orange, pink, green"
)

# Validate user input
if not user_guess or user_guess.lower() not in colors:
    print("Invalid color! Please restart and choose from the given options.")
    screen.bye()  # Close the Turtle window
else:
    race_onn = True

# Create turtles only if user input is valid
if race_onn:
    for turtle_index in range(6):
        tim = turtle.Turtle(shape="turtle")
        tim.color(colors[turtle_index])
        tim.penup()
        tim.goto(x=-250, y=y_positions[turtle_index])
        all_turtles.append(tim)
        tim.speed("fastest")

# Start race
while race_onn:
    for turtle in all_turtles:
        if turtle.xcor() > 245:
            race_onn = False
            winning_turtle = turtle.pencolor()

            if winning_turtle.lower() == user_guess.lower():
                print(f"🎉 You guessed right! {winning_turtle} is the winner!")
            else:
                print(f"❌ Wrong guess! {winning_turtle} is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
