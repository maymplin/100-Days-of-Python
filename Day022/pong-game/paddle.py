from turtle import Turtle, Screen

PADDLE_SIZE = (5, 1)
INITIAL_POSITION = (350, 0)
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Paddle:
    def __init__(self):
        self.paddle = Turtle(shape="square")
        self.paddle.shapesize(5, 1)
        self.paddle.penup()
        self.paddle.setpos(INITIAL_POSITION)
        self.paddle.color("white")
        self.x_pos = self.paddle.xcor()
        self.y_pos = self.paddle.ycor()

    def go_up(self):
        self.y_pos += MOVE_DISTANCE
        self.paddle.goto(self.x_pos, self.y_pos)

    def go_down(self):
        self.y_pos -= MOVE_DISTANCE
        self.paddle.goto(self.x_pos, self.y_pos)