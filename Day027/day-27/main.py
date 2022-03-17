# https://www.udemy.com/course/100-days-of-code/learn/lecture/20781156
# https://www.udemy.com/course/100-days-of-code/learn/lecture/20781168

import tkinter


def button_clicked():
    # print("I got clicked")
    my_label["text"] = entry.get()


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20) # can also pad around individual widgets


# Label
# https://docs.python.org/3/library/tkinter.html#the-packer
# http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# pack, place, grid
# pack - side="center", "left", etc.
# place - precision placement
# grid - in columns and rows; relative to other components
# N.B. cannot mix grid and pack in the same program
my_label = tkinter.Label(text="I am a Label", font=("Ariel", 24, "bold"))
# my_label["text"] = "New Text"           # this and the next line my_label.config() do the same thing
my_label.config(text="New text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="Click Me 2", command=button_clicked)
new_button.grid(column=3, row=0)

# Entry
entry = tkinter.Entry(width=30)
# Add placeholder text
entry.insert(tkinter.END, string="Some text to begin with")
# Gets text in entry
print(entry.get())
# entry.pack()
entry.grid(column=3, row=2)

window.mainloop()

