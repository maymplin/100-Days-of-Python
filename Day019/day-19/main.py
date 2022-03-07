# https://www.udemy.com/course/100-days-of-code/learn/lecture/20337031
# https://www.udemy.com/course/100-days-of-code/learn/lecture/20337245
# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# tim.shape("turtle")
# tim.color("orange")


def move_forward():
    tim.forward(1)


def move_backward():
    tim.backward(1)


def turn_counter_clock():
    tim.right(1)
    tim.forward(1)


def turn_clockwise():
    tim.left(1)
    tim.forward(1)


def clear_drawing():
    tim.reset()


screen.listen()

screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_counter_clock, "a")
screen.onkeypress(turn_clockwise, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()
