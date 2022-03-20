import tkinter

FONT = ("Ariel", 10, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


# https://www.geeksforgeeks.org/python-append-to-a-file/
def save_password_to_file():
    with open("password.txt", "a") as file:
        website = website_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        file.write(f"{website} | {username} | {password}\n")


def clear_entries():
    website_entry.delete(0, tkinter.END)
    website_entry.focus()
    password_entry.delete(0, tkinter.END)


def add_button_clicked():
    save_password_to_file()
    clear_entries()


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

username_label = tkinter.Label(text="Email/Username:", bg="white", font=FONT)
username_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:", bg="white", font=FONT)
password_label.grid(column=0, row=3)

# Entries
# https://tkdocs.com/tutorial/widgets.html#entry
website_entry = tkinter.Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

username_entry = tkinter.Entry(width=35)
username_entry.insert(0, "mlin42sv@gmail.com")  # pre-populate field
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = tkinter.Entry()
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
generate_password_button = tkinter.Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = tkinter.Button(text="Add", width=35)
add_button.config(command=add_button_clicked)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")


window.mainloop()
