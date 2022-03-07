# https://www.udemy.com/course/100-days-of-code/learn/lecture/20356591
import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

# print(snake.shapesize(1, 3, 1))

game_is_on = True
snake = Snake()

while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move_forward()




screen.exitonclick()