# https://www.udemy.com/course/100-days-of-code/learn/lecture/20338889

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)     # width, height
# screen.bgpic("racetrack.png")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]


def turtle_setup(index):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    if index < 3:
        new_turtle.goto(-240, 30*(index + 1))
    elif index > 3:
        new_turtle.goto(-240, -30*(index - 3))
    else:
        new_turtle.goto(-240, 0)

    return new_turtle


def move_forward(the_turtle):
    steps = randint(0, 10)
    the_turtle.forward(steps)


def race():
    user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

    turtles = []
    is_race_on = True

    for i in range(7):
        turtles.append(turtle_setup(i))

    while is_race_on:
        turtle_index = randint(0, len(turtles) - 1)
        move_forward(turtles[turtle_index])

        if turtles[turtle_index].xcor() >= 230:
            is_race_on = False

    winning_color = turtles[turtle_index].pencolor()

    if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
    else:
        print(f"You've lost! The {winning_color} turtle is the winner!")


race()

screen.exitonclick()




