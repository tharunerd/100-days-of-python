# ---------------------------- IMPORTS ------------------------------- #
<<<<<<< HEAD
from tkinter import Tk, Canvas, Button, PhotoImage
import pandas as pd
=======
from tkinter import *
import pandas
>>>>>>> 3538a6b (Flash Card App (French → English))
import random
import os

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 20, "italic")
FONT_WORD = ("Arial", 30, "bold")
<<<<<<< HEAD
FLIP_DELAY_MS = 3000

# ---------------------------- PATH SETUP ------------------------------- #
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGE_DIR = os.path.join(BASE_DIR, "images")

FRENCH_WORDS_PATH = os.path.join(DATA_DIR, "french_words.csv")
WORDS_TO_LEARN_PATH = os.path.join(DATA_DIR, "words_to_learn.csv")

# ---------------------------- GLOBAL STATE ------------------------------- #
=======

# ---------------------------- PATH SETUP ------------------------------- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

WORDS_TO_LEARN_PATH = os.path.join(DATA_DIR, "words_to_learn.csv")
FRENCH_WORDS_PATH = os.path.join(DATA_DIR, "french_words.csv")

# ---------------------------- GLOBAL VARIABLES ------------------------------- #
>>>>>>> 3538a6b (Flash Card App (French → English))
current_card = {}
to_learn = []

# ---------------------------- LOAD DATA ------------------------------- #
<<<<<<< HEAD
def load_data():
    """Load words to learn or fallback to original dataset."""
    try:
        data = pd.read_csv(WORDS_TO_LEARN_PATH)
    except FileNotFoundError:
        data = pd.read_csv(FRENCH_WORDS_PATH)
    return data.to_dict(orient="records")

to_learn = load_data()

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    """Show the next random French word."""
    global current_card, flip_timer

    if not to_learn:
        canvas.itemconfig(card_title, text="🎉 Done!", fill="black")
        canvas.itemconfig(card_word, text="All words learned", fill="black")
=======
try:
    data = pandas.read_csv(WORDS_TO_LEARN_PATH)
    to_learn = data.to_dict(orient="records")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv(FRENCH_WORDS_PATH)
    to_learn = data.to_dict(orient="records")

# ---------------------------- FUNCTIONS ------------------------------- #
def next_card():
    global current_card, flip_timer

    if len(to_learn) == 0:
        canvas.itemconfig(card_title, text="Done!", fill="black")
        canvas.itemconfig(card_word, text="All words learned 🎉", fill="black")
>>>>>>> 3538a6b (Flash Card App (French → English))
        canvas.itemconfig(card_background, image=card_front_img)
        return

    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

<<<<<<< HEAD
    flip_timer = window.after(FLIP_DELAY_MS, flip_card)


def flip_card():
    """Flip card to show English meaning."""
=======
    flip_timer = window.after(3000, flip_card)


def flip_card():
>>>>>>> 3538a6b (Flash Card App (French → English))
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
<<<<<<< HEAD
    """Remove known word and save progress."""
    to_learn.remove(current_card)
    pd.DataFrame(to_learn).to_csv(WORDS_TO_LEARN_PATH, index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(FLIP_DELAY_MS, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file=os.path.join(IMAGE_DIR, "card_front.png"))
card_back_img = PhotoImage(file=os.path.join(IMAGE_DIR, "card_back.png"))
=======
    to_learn.remove(current_card)

    # Save progress
    pandas.DataFrame(to_learn).to_csv(WORDS_TO_LEARN_PATH, index=False)

    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy - Language Learning App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file=os.path.join(IMAGES_DIR, "card_front.png"))
card_back_img = PhotoImage(file=os.path.join(IMAGES_DIR, "card_back.png"))
>>>>>>> 3538a6b (Flash Card App (French → English))

card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=FONT_TITLE)
card_word = canvas.create_text(400, 263, text="", font=FONT_WORD)

canvas.grid(row=0, column=0, columnspan=2)

# Buttons
<<<<<<< HEAD
wrong_img = PhotoImage(file=os.path.join(IMAGE_DIR, "wrong.png"))
right_img = PhotoImage(file=os.path.join(IMAGE_DIR, "right.png"))

unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=right_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# ---------------------------- START APP ------------------------------- #
=======
cross_image = PhotoImage(file=os.path.join(IMAGES_DIR, "wrong.png"))
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=os.path.join(IMAGES_DIR, "right.png"))
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# ---------------------------- START ------------------------------- #
>>>>>>> 3538a6b (Flash Card App (French → English))
next_card()
window.mainloop()