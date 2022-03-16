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
    my_label["text"] = user_input.get()


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
user_input = tkinter.Entry(width=10)
user_input.pack()


window.mainloop()

