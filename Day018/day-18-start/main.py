# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")

# draw a square
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# draw a dashed line
# for _ in range(15):
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.pendown()

screen = Screen()
screen.exitonclick()

