# https://www.udemy.com/course/100-days-of-code/learn/lecture/20356591
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

# print(snake.shapesize(1, 3, 1))

is_game_over = False
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while not is_game_over:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()
    scoreboard.keep_score(snake, food)
    is_game_over = scoreboard.is_game_over(snake)


screen.exitonclick()