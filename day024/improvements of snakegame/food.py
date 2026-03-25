import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        # self.speed("fastest")
        self.refresh()  # ✅ Place food at a random position initially

    def refresh(self):
        """Move the food to a new random position."""
        new_x = random.randint(-260, 260)
        new_y = random.randint(-220, 220)
        self.goto(new_x, new_y)