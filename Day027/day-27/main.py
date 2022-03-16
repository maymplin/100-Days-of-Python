# https://www.udemy.com/course/100-days-of-code/learn/lecture/20781156

import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)


def button_clicked():
    # print("I got clicked")
    my_label["text"] = entry.get()


# Label
# https://docs.python.org/3/library/tkinter.html#the-packer
# http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# pack, place, grid
# pack - side="center", "left", etc.
# place - precision placement
# grid -
my_label = tkinter.Label(text="I am a Label", font=("Ariel", 24, "bold"))
# my_label["text"] = "New Text"           # this and the next line my_label.config() do the same thing
my_label.config(text="New text")
# my_label.pack()
my_label.place(x=0, y=0)

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
entry = tkinter.Entry(width=30)
# Add placeholder text
entry.insert(tkinter.END, string="Some text to begin with")
# Gets text in entry
print(entry.get())
entry.pack()


window.mainloop()

