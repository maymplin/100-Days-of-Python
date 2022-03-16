# https://www.udemy.com/course/100-days-of-code/learn/lecture/20781156

import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

# Label

# https://docs.python.org/3/library/tkinter.html#the-packer
# http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
my_label = tkinter.Label(text="I am a Label", font=("Ariel", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"           # this and the next line my_label.config() do the same thing
my_label.config(text="Another text")


# Button
def button_clicked():
    # print("I got clicked")
    my_label["text"] = entry.get()


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
entry = tkinter.Entry(width=30)
# Add placeholder text
entry.insert(tkinter.END, string="Some text to begin with")
# Gets text in entry
print(entry.get())
entry.pack()

# Text
text = tkinter.Text(height=5, width=30)
# Puts cursor in textbox
text.focus()
# Adds some text to begin with (placeholder)
text.insert(tkinter.END, "Example of multi-line entry")
# Get's current value in textbook at line 1, character 0
print(text.get("1.0", tkinter.END))
text.pack()


# Spinbox
# A Spinbox widget allows you to select a value from a set of values.
# https://www.pythontutorial.net/tkinter/tkinter-spinbox/
def spinbox_used():
    # Gets the current value in spinbox
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value
def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked; otherwise 0
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio value is checked
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Berry", "Carambola", "Date", "Guava"]

for fruit in fruits:
    listbox.insert(fruits.index(fruit), fruit)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()

