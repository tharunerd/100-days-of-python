import turtle
import time
from snake import Snake
from food import Food
from score import Scoreboard

# ------------------------- Screen Setup -------------------------
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Snake Game - No High Score Edition")
screen.tracer(0)

# ------------------------- Draw Visible Walls -------------------------
border = turtle.Turtle()
border.hideturtle()
border.speed("fastest")
border.color("white")
border.penup()
border.goto(-280, -280)
border.pendown()
border.pensize(3)

for _ in range(4):
    border.forward(560)
    border.left(90)

# ------------------------- Game Objects -------------------------
snake = Snake()
food = Food()
scoreboard = Scoreboard()  # Only shows current score

# ------------------------- Controls -------------------------
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# ------------------------- Game Loop -------------------------
game_is_on = True
game_speed = 0.12

while game_is_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()

    # --------------------- Eat Food ---------------------
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()

        if game_speed > 0.05:
            game_speed -= 0.005

    # --------------------- Wall Collision ---------------------
    if (snake.head.xcor() > 265 or snake.head.xcor() < -265 or
        snake.head.ycor() > 265 or snake.head.ycor() < -265):

        scoreboard.game_over()
        game_is_on = False   # Stop loop but DO NOT close window

    # --------------------- Tail Collision ---------------------
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False
            break

# Window stays open until clicked
screen.exitonclick()