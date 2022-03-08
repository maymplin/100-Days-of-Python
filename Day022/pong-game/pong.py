from turtle import Turtle, Screen
from paddle import Paddle


class Pong:
    def __init__(self):
        self.screen = Screen()
        self.screen.screensize(800, 600, "black")
        self.screen.title("Pong")
        self.paddle = Paddle()
        self.is_game_over = False
        self.start_game()
        self.screen.exitonclick()
        
    def start_game(self):
        self.screen.tracer()
        self.screen.listen()
        self.screen.onkey(self.paddle.go_up, "Up")
        self.screen.onkey(self.paddle.go_down, "Down")

        while not self.is_game_over:
            self.screen.update()


