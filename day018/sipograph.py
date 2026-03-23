import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)














# def make_shape(no_of_sides):
#     angle = 360 / no_of_sides
#     for _ in range(no_of_sides):
#         tim.forward(60)
#         tim.right(angle)
# for shape in range (4, 6):
#     tim.color(random.choice(colours))
#     make_shape(shape)
