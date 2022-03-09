from turtle import Turtle
import random

MOVE_DISTANCE = 10
INITIAL_SPEED = 0.05


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setheading(random.randint(1, 89))
        self.move_speed = INITIAL_SPEED

    def move(self, left_paddle, right_paddle, scoreboard):
        if self.xcor() > 450:
            self.setheading(random.randint(91, 269))
            scoreboard.l_point()
            self.goto(0, 0)
            self.move_speed = INITIAL_SPEED
        elif self.xcor() < -450:
            self.setheading(random.choice((random.randint(1, 89), random.randint(271, 359))))
            scoreboard.r_point()
            self.goto(0, 0)
            self.move_speed = INITIAL_SPEED
        else:
            self.hit_right_paddle(right_paddle)
            self.hit_left_paddle(left_paddle)
            self.hit_top_or_bottom()
        self.forward(MOVE_DISTANCE)

    def hit_right_paddle(self, right_paddle):
        if self.distance(right_paddle) < 50 and self.xcor() > 320:
            self.setheading(180 - self.heading())
            self.move_speed *= 0.9
            self.forward(MOVE_DISTANCE*3)

    def hit_left_paddle(self, left_paddle):
        if self.distance(left_paddle) < 50 and self.xcor() < -320:
            self.setheading(180 - self.heading())
            self.move_speed *= 0.9
            self.forward(MOVE_DISTANCE*3)

    def hit_top_or_bottom(self):
        if self.ycor() >= 380 or self.ycor() <= -380:
            self.setheading(360 - self.heading())

    # def out_of_bound(self):
    #     if self.xcor() > 400 or self.xcor() < -400:
    #         self.goto(0, 0)
    #         self.setheading(360 - self.heading)
