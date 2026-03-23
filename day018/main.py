import os
import random
from random import choice
import turtle

# ---- Optional: extract colors using colorgram if available ----
def extract_colors_from_image(img_path, n=20):
    """
    Try to extract n colors (as (r,g,b) tuples) from an image using colorgram.
    Falls back to a predefined palette if colorgram isn't installed or file missing.
    """
    try:
        import colorgram
        # Normalize path separators for cross-platform compatibility
        img_path = os.path.normpath(img_path)
        if not os.path.isfile(img_path):
            raise FileNotFoundError(f"Image not found: {img_path}")

        colours = colorgram.extract(img_path, n)
        rgb_colors = []
        for c in colours:
            r, g, b = c.rgb.r, c.rgb.g, c.rgb.b
            rgb_colors.append((r, g, b))
        # Filter out near-white/near-black extremes if desired
        cleaned = [
            (r, g, b) for (r, g, b) in rgb_colors
            if not (r > 240 and g > 240 and b > 240)  # skip whites
            and not (r < 15 and g < 15 and b < 15)    # skip blacks
        ]
        # Ensure we have something
        return cleaned or rgb_colors or None
    except Exception as e:
        # Any issue (module missing, file error, etc.) falls back to default palette
        print(f"[Info] Using fallback palette. Reason: {e}")
        return None

# ---- Configurable parameters ----
IMG_PATH = r"day018/image.jpeg"   # Use forward slash or raw string; avoid backslash escapes
DOT_COUNT_X = 10                  # columns
DOT_COUNT_Y = 10                  # rows
DOT_SIZE = 20                     # diameter of each dot (in pixels)
DOT_SPACING = 50                  # distance between dot centers
MARGIN = 50                       # extra margin from center to first dot

# ---- Try extracting colors, else use a manual list ----
extracted = extract_colors_from_image(IMG_PATH, n=30)
if extracted:
    color_list = extracted
else:
    # Your manual fallback palette (feel free to tweak)
    color_list = [
        (202, 23, 34), (123, 67, 8), (123, 34, 98),
        (56, 78, 89), (12, 34, 56), (34, 34, 56), (24, 35, 56),
        (231, 162, 80), (40, 112, 79), (184, 72, 94),
        (219, 208, 96), (65, 148, 207), (102, 78, 173)
    ]

# ---- Turtle setup ----
turtle.colormode(255)
tim = turtle.Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")

# Compute total width/height of grid to center it on screen
total_width = (DOT_COUNT_X - 1) * DOT_SPACING
total_height = (DOT_COUNT_Y - 1) * DOT_SPACING

# Starting position: bottom-left of the grid (centered overall)
start_x = -total_width / 2
start_y = -total_height / 2

# Move to start
tim.setheading(0)
tim.goto(start_x, start_y)

# ---- Draw the grid of dots ----
for row in range(DOT_COUNT_Y):
    for col in range(DOT_COUNT_X):
        tim.dot(DOT_SIZE, choice(color_list))
        tim.forward(DOT_SPACING)
    # Move to the next row
    tim.setx(start_x)
    tim.sety(start_y + (row + 1) * DOT_SPACING)

# ---- Keep window open until click ----
screen = turtle.Screen()
screen.title("Day 18 - Hirst Style Dot Grid")
screen.exitonclick()