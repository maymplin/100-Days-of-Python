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
from os.path import exists
from os import remove
from tkinter import messagebox

# --------------------------- CONSTANTS ------------------------------ #

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# ------------------------- GLOBAL VARIABLES -------------------------- #

new_word = ""
timer = None
fr_eng_dict = None


# --------------------------- FLIP CARD ------------------------------- #

def find_english():
    return new_word["English"]


def display_back_of_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=find_english(), fill="white")
    canvas.itemconfig(canvas_img, image=back_img)
    window.after_cancel(timer)


# ----------------------- TRACK UNKNOWN WORDS ------------------------ #

def play_again():
    return tkinter.messagebox.askyesno("Play Again?", f"You know all the words already. Good job!\n"
                                                      f"Do you want to practice from the beginning again?")


def reset_word_dict():
    global fr_eng_dict
    fr_eng_dict = pd.read_csv("data/french_words.csv").to_dict(orient="record")


if exists("unknown_words.csv"):
    df = pd.read_csv("unknown_words.csv")
    fr_eng_dict = df.to_dict(orient="record")
else:
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
    reset_word_dict()


def update_unknown_words_file():
    updated_df = pd.DataFrame(fr_eng_dict)
    updated_df.to_csv("unknown_words.csv", index=False)


def remove_known_word():
    window.after_cancel(timer)
    fr_eng_dict.remove(new_word)
    update_unknown_words_file()
    display_new_word()

# ------------------------- GENERATE WORDS ---------------------------- #


def pick_random_word():
    if len(fr_eng_dict) == 0:
        if play_again():
            reset_word_dict()
            return random.choice(fr_eng_dict)
        else:
            canvas.delete("all")
            window.quit()
            remove("unknown_words.csv")
    else:
        return random.choice(fr_eng_dict)


def display_new_word():
    global new_word, timer
    new_word = pick_random_word()
    canvas.itemconfig(title_text, text="French", fill="black")
    try:
        canvas.itemconfig(word_text, text=new_word["French"], fill="black")
    except TypeError:
        print("To play, you must choose to start game again.")
    else:
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
right_button = tkinter.Button(image=right_img, highlightthickness=0, command=remove_known_word)
right_button.grid(row=1, column=1)

display_new_word()

window.mainloop()
