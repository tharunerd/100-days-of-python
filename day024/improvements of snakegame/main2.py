import turtle
import time
from snake import Snake
from food import Food
from score import Scoreboard

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # ✅ Turn off auto-refresh

# Objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()  # ✅ Manual screen update
    time.sleep(0.2)  # ✅ Smooth movement
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:  # ✅ Corrected condition
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (
            snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 230 or snake.head.ycor() < -230
    ):
        scoreboard.reset()
        snake.reset()

    # Detect collision with itself
    for segment in snake.segments[1:]:  # Exclude head
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()