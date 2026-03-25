import turtle
import os

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.update_scoreboard()

    def load_high_score(self):
        """Load high score from file, or initialize to 0 if file is empty or missing."""
        if not os.path.exists("data.txt") or os.path.getsize("data.txt") == 0:
            with open("data.txt", "w") as file:
                file.write("0")
            return 0
        with open("data.txt") as data:
            content = data.read().strip()
            return int(content) if content else 0

    def update_scoreboard(self):
        """Clear and rewrite the score display."""
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """Increase the score and update the display."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """Reset the score and update high score if needed."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        """Display game over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
        self.goto(0, -30)
        self.write(f"Final Score: {self.score}", align="center", font=("Arial", 18, "normal"))
