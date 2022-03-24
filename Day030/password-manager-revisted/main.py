import tkinter
from tkinter import messagebox
import string
import random
import json

FONT = ("Ariel", 10, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters_lowercase = list(string.ascii_lowercase)
letters_uppercase = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_lower = [random.choice(letters_lowercase) for _ in range(random.randint(8, 10))]
    password_upper = [random.choice(letters_uppercase) for _ in range(random.randint(2, 3))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_lower + password_upper + password_numbers + password_symbols

    random.shuffle(password_list)

    new_password = ''.join(password_list)
    password_entry.insert(0, string=f'{new_password}')
    password_entry.clipboard_append(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def display_confirmation():
    if len(username_entry.get()) > 0 and len(password_entry.get()) > 0:
        save_password_to_file()
        clear_entries()
    else:
        messagebox.showinfo(title="Oops", message="Website and username/email must not be empty.")
    

# https://www.geeksforgeeks.org/python-append-to-a-file/
def save_password_to_file():
    website = website_entry.get()
    url = url_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "url": url,
            "username": username,
            "password": password,
        }
    }

    with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)

        # file.write(f"{website} | {url} | {username} | {password}\n")


# https://tkdocs.com/tutorial/widgets.html#entry
def clear_entries():
    website_entry.delete(0, tkinter.END)
    website_entry.focus()
    password_entry.delete(0, tkinter.END)


def add_button_clicked():
    display_confirmation()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:", bg="white", font=FONT)
website_label.grid(column=0, row=1)

url_label = tkinter.Label(text="URL:", bg="white", font=FONT)
url_label.grid(column=0, row=2)

username_label = tkinter.Label(text="Email/Username:", bg="white", font=FONT)
username_label.grid(column=0, row=3)

password_label = tkinter.Label(text="Password:", bg="white", font=FONT)
password_label.grid(column=0, row=4)

# Entries
# https://tkdocs.com/tutorial/widgets.html#entry
website_entry = tkinter.Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

url_entry = tkinter.Entry(width=35)
url_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

username_entry = tkinter.Entry(width=35)
username_entry.insert(0, "me@gmail.com")  # pre-populate field
username_entry.grid(column=1, row=3, columnspan=2, sticky="EW")

password_entry = tkinter.Entry()
password_entry.grid(column=1, row=4, sticky="EW")

# Buttons
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=4, sticky="EW")

add_button = tkinter.Button(text="Add", width=35)
add_button.config(command=add_button_clicked)
add_button.grid(column=1, row=5, columnspan=2, sticky="EW")


window.mainloop()
