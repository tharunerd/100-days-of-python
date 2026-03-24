
import random
import turtle

# ---------- Configuration ----------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
TRACK_MARGIN = 40
FINISH_LINE_OFFSET = 50
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

# Step size range (each tick a turtle advances by a random integer in this range)
STEP_MIN = 2
STEP_MAX = 10

# ---------- Setup Screen ----------
screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle Race - Day 18 Fun!")

# Ask the user to bet on a turtle color (optional)
bet = screen.textinput(title="Make your bet",
                       prompt=f"Which color turtle will win? Choose from:\n{', '.join(COLORS)}").strip().lower() if screen else None

# ---------- Draw Track ----------
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed("fastest")
drawer.penup()

# Start/Finish lines
start_x = -SCREEN_WIDTH // 2 + TRACK_MARGIN
finish_x = SCREEN_WIDTH // 2 - FINISH_LINE_OFFSET

# Draw start line
drawer.goto(start_x, SCREEN_HEIGHT//2 - TRACK_MARGIN)
drawer.setheading(-90)
drawer.pendown()
drawer.pensize(3)
drawer.color("gray20")
drawer.forward(SCREEN_HEIGHT - 2*TRACK_MARGIN)
drawer.penup()

# Draw finish line
drawer.goto(finish_x, SCREEN_HEIGHT//2 - TRACK_MARGIN)
drawer.setheading(-90)
drawer.pendown()
drawer.color("black")
for _ in range((SCREEN_HEIGHT - 2*TRACK_MARGIN) // 20):
    drawer.forward(10)
    drawer.penup()
    drawer.forward(10)
    drawer.pendown()
drawer.penup()

# Lane markers (dashed)
lane_count = len(COLORS)
top_y = (lane_count - 1) * 40 / 2  # lane spacing = 40
drawer.color("lightgray")
for i in range(lane_count):
    y = top_y - i * 40
    drawer.goto(start_x, y - 20)
    drawer.setheading(0)
    drawer.pendown()
    for _ in range((finish_x - start_x) // 20):
        drawer.forward(10)
        drawer.penup()
        drawer.forward(10)
        drawer.pendown()
    drawer.penup()

# ---------- Create Racers ----------
racers = []
for idx, color in enumerate(COLORS):
    racer = turtle.Turtle(shape="turtle")
    racer.color(color)
    racer.penup()
    racer.speed("fastest")
    # Position turtles at the start line, each on its own lane
    y = top_y - idx * 40
    racer.goto(start_x - 20, y)     # a tiny bit before start line for a nice look
    racer.setheading(0)
    racers.append(racer)

# ---------- Countdown ----------
countdown = turtle.Turtle()
countdown.hideturtle()
countdown.penup()
countdown.goto(0, SCREEN_HEIGHT//2 - 60)
countdown.write("3", align="center", font=("Arial", 24, "bold"))
screen.update() if hasattr(screen, "update") else None
screen.ontimer(lambda: countdown.clear() or countdown.write("2", align="center", font=("Arial", 24, "bold")), 500)
screen.ontimer(lambda: countdown.clear() or countdown.write("1", align="center", font=("Arial", 24, "bold")), 1000)
screen.ontimer(lambda: countdown.clear() or countdown.write("GO!", align="center", font=("Arial", 24, "bold")), 1500)

# Small delay before starting movement
def start_race():
    countdown.clear()

    winner = None
    running = True
    while running:
        for turt in racers:
            step = random.randint(STEP_MIN, STEP_MAX)
            turt.forward(step)
            if turt.xcor() >= finish_x:
                winner = turt.pencolor()
                running = False
                break

    # Show result
    announcer = turtle.Turtle()
    announcer.hideturtle()
    announcer.penup()
    announcer.goto(0, -SCREEN_HEIGHT//2 + 60)

    if bet:
        if bet == winner:
            announcer_color = "green"
            msg = f"🏆 {winner.capitalize()} wins! You guessed right! 🎉"
        else:
            announcer_color = "red"
            msg = f"🏁 {winner.capitalize()} wins! Your bet ({bet}) lost. Try again!"
    else:
        announcer_color = "black"
        msg = f"🏁 {winner.capitalize()} wins!"

    announcer.color(announcer_color)
    announcer.write(msg, align="center", font=("Arial", 18, "bold"))

# Start race after the countdown finishes
screen.ontimer(start_race, 1800)

# Keep window open until click
screen.exitonclick()