# ---------------------------- IMPORTS ------------------------------- #
from tkinter import Tk, Canvas, Button, PhotoImage
import pandas as pd
import random
import os

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 20, "italic")
FONT_WORD = ("Arial", 30, "bold")
FLIP_DELAY_MS = 3000

# ---------------------------- PATH SETUP ------------------------------- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGE_DIR = os.path.join(BASE_DIR, "images")

WORDS_TO_LEARN_PATH = os.path.join(DATA_DIR, "words_to_learn.csv")
FRENCH_WORDS_PATH = os.path.join(DATA_DIR, "french_words.csv")

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
current_card = {}
to_learn = []

# ---------------------------- LOAD DATA ------------------------------- #
try:
    data = pd.read_csv(WORDS_TO_LEARN_PATH)
except (FileNotFoundError, pd.errors.EmptyDataError):
    data = pd.read_csv(FRENCH_WORDS_PATH)

to_learn = data.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_card, flip_timer

    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text="Done!", fill="black")
        canvas.itemconfig(card_word, text="All words learned 🎉", fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        return

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(FLIP_DELAY_MS, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)

    # Save progress
    pd.DataFrame(to_learn).to_csv(WORDS_TO_LEARN_PATH, index=False)

    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy - Language Learning App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(FLIP_DELAY_MS, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file=os.path.join(IMAGE_DIR, "card_front.png"))
card_back_img = PhotoImage(file=os.path.join(IMAGE_DIR, "card_back.png"))

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=FONT_TITLE)
card_word = canvas.create_text(400, 263, text="", font=FONT_WORD)

canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file=os.path.join(IMAGE_DIR, "wrong.png"))
right_img = PhotoImage(file=os.path.join(IMAGE_DIR, "right.png"))

unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=right_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# ---------------------------- START ------------------------------- #
next_card()
window.mainloop()