import tkinter

FONT = ("Ariel",15, "normal")
BACKGROUND_COLOR = "white"

window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(300, 200)
window.config(padx=20, pady=20)
window.configure(bg=BACKGROUND_COLOR)


def button_clicked():
    result = float(miles_entry.get())*1.60934
    km_value_label.config(text=str(round(result, 2)))


miles_entry = tkinter.Entry(width=18)
miles_entry.insert(tkinter.END, string="0")
miles_entry.grid(column=1, row=0)

miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.config(padx=10, bg=BACKGROUND_COLOR)
miles_label.grid(column=2, row=0)

is_equal_to_label = tkinter.Label(text="is equal to", font=FONT)
is_equal_to_label.config(padx=10, pady=5, bg=BACKGROUND_COLOR)
is_equal_to_label.grid(column=0, row=1)

km_value_label = tkinter.Label(text="0", font=FONT)
km_value_label.config(padx=15, pady=5, bg=BACKGROUND_COLOR)
km_value_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km", font=FONT)
km_label.config(bg=BACKGROUND_COLOR)
km_label.grid(column=2, row=1)

calculate_button = tkinter.Button(text="Calculate", font=FONT)
calculate_button.config(padx=10, bg=BACKGROUND_COLOR, command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()