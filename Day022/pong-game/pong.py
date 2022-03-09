from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

SCREEN_X = 800
SCREEN_Y = 600


class Pong:
    def __init__(self):
        self.screen = Screen()
        self.screen.screensize(SCREEN_X, SCREEN_Y, "black")
        self.screen.title("Pong")
        self.scoreboard = Scoreboard()
        self.paddle_left = Paddle("left")
        self.paddle_right = Paddle("right")
        self.ball = Ball()
        self.is_game_over = False
        self.start_game()
        self.screen.exitonclick()
        
    def start_game(self):
        self.screen.tracer()
        self.screen.listen()
        self.screen.onkeypress(self.paddle_right.go_up, "Up")
        self.screen.onkeypress(self.paddle_right.go_down, "Down")
        self.screen.onkeypress(self.paddle_left.go_up, "w")
        self.screen.onkeypress(self.paddle_left.go_down, "s")

        while not self.is_game_over:
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.ball.move(self.paddle_left, self.paddle_right, self.scoreboard)






