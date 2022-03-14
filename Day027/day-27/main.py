import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

# Label

# https://docs.python.org/3/library/tkinter.html#the-packer
# http://tcl.tk/man/tcl8.6/TkCmd/pack.htm
my_label = tkinter.Label(text="I am a Label", font=("Ariel", 24, "bold"))
my_label.pack()


window.mainloop()

