# References
# https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists
# https://github.com/hermitdave/FrequencyWords/tree/master/content/2018
# https://www.google.co.uk/sheets/about/
# https://www.opensubtitles.org/en/search/subs
# https://support.google.com/docs/answer/3093331?hl=en-GB
# https://cloud.google.com/translate/docs/languages?hl=en

import tkinter
import pandas as pd
import random

# --------------------------- CONSTANTS ------------------------------ #

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# ------------------------- GLOBAL VARIABLES -------------------------- #

next_word = ""
timer = None


# --------------------------- FLIP CARD ------------------------------- #

def find_english():
    return fr_eng_dict[next_word]


def display_back_of_card():
    english_word = find_english()
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word, fill="white")
    canvas.itemconfig(canvas_img, image=back_img)
    window.after_cancel(timer)


# ------------------------- GENERATE WORDS ---------------------------- #

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
data = pd.read_csv("data/french_words.csv")
french_words = data.French.tolist()
english_words = data.English.tolist()
fr_eng_dict = dict(zip(french_words, english_words))


def pick_random_word():
    return random.choice(french_words)


def display_new_word():
    global next_word, timer
    next_word = pick_random_word()
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=next_word, fill="black")
    canvas.itemconfig(canvas_img, image=front_img)
    timer = window.after(3000, display_back_of_card)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

# canvas
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = tkinter.PhotoImage(file="images/card_front.png")
back_img = tkinter.PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=front_img)
title_text = canvas.create_text(400, 150, text="French", fill="black", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text="", fill="black", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, command=display_new_word)
wrong_button.grid(row=1, column=0)

right_img = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_img, highlightthickness=0, command=display_new_word)
right_button.grid(row=1, column=1)

display_new_word()

window.mainloop()
