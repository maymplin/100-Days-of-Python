import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.timer = None

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # label
        self.score_label = tkinter.Label(text="Score: 0", font=("Ariel", 12, "normal"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Question",
            fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_img, bg=THEME_COLOR, highlightthickness=0,
                                          command=self.true_button_clicked)
        self.true_button.grid(row=2, column=0)

        false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_img, bg=THEME_COLOR, highlightthickness=0,
                                           command=self.false_button_clicked)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def buttons_state(self, state:str):
        self.true_button.config(state=state)
        self.false_button.config(state=state)

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.timer is not None:
            self.window.after_cancel(self.timer)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You have reached the end of the quiz.")
            self.buttons_state(tkinter.DISABLED)

    def true_button_clicked(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_button_clicked(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.timer = self.window.after(800, self.get_next_question)