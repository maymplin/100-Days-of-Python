import tkinter

FONT = ("Ariel", 10, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:", bg="white", font=FONT)
website_label.grid(column=0, row=1)

username_label = tkinter.Label(text="Email/Username", bg="white", font=FONT)
username_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:", bg="white", font=FONT)
password_label.grid(column=0, row=3)

website_entry = tkinter.Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

username_entry = tkinter.Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = tkinter.Entry()
password_entry.grid(column=1, row=3, sticky="EW")

generate_password_button = tkinter.Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = tkinter.Button(text="Add", width=35)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
