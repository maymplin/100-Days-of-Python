# https://colorhunt.co/
# https://www.youtube.com/watch?v=UZX5kH72Yx4
import tkinter
import math


def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="25:00")
    check_label.config(text="")

    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps

    reps += 1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    # window.attributes('-topmost', 1)

    if reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
        focus_window("off")
    elif reps == 8:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
        focus_window("on")
        reps = 0
    else:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        focus_window("on")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f'{count_min:02}:{count_sec:02}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        window.bell()
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

rest_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
rest_button.grid(column=2, row=2)

check_label = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 17, "bold"), highlightthickness=0)
check_label.grid(column=1, row=3)

window.mainloop()
