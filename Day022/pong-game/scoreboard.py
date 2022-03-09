from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.speed("fastest")
        self.print_score()

    def l_point(self):
        self.left_score += 1
        self.clear()
        self.print_score()

    def r_point(self):
        self.right_score += 1
        self.clear()
        self.print_score()

    def print_score(self):
        self.goto(-250, 300)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(250, 300)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)