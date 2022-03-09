from turtle import Turtle, Screen

INITIAL_X = 350
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SCREEN_X = 800
SCREEN_Y = 600


class Paddle(Turtle):
    def __init__(self, paddle_position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.speed("fast")
        self.determine_left_or_right(paddle_position)
        self.color("white")
        self.x_pos = self.xcor()
        self.y_pos = self.ycor()

    def determine_left_or_right(self, paddle_pos):
        if paddle_pos.lower() == "left":
            self.goto(-INITIAL_X, 0)
        else:
            self.goto(INITIAL_X, 0)

    def go_up(self):
        if self.y_pos < SCREEN_Y//2 + 50:
            self.y_pos += MOVE_DISTANCE
            self.goto(self.x_pos, self.y_pos)

    def go_down(self):
        if self.y_pos > (-SCREEN_Y)//2 - 50:
            self.y_pos -= MOVE_DISTANCE
            self.goto(self.x_pos, self.y_pos)