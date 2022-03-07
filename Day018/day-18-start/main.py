# https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen, colormode
from random import randint, choice

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")


# 166 - draw a square
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# 168 - draw a dashed line
# for _ in range(15):
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.pendown()


# 169 - draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# colors = ["red", "dark orange", "gold", "dark green", "blue", "indigo", "black", "deep pink"]
#
#
# def draw_shape(num_of_sides):
#     each_angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(each_angle)
#
#
# for i in range(3, 11):
#     timmy_the_turtle.pencolor(colors[i - 3])
#     draw_shape(i)


# 170 - generate a random walk
# colormode(255)
#
#
# def random_color():
#     return randint(0, 255), randint(0, 255), randint(0, 255)
#
#
# timmy_the_turtle.pensize(5)
# timmy_the_turtle.speed("fastest")
# for _ in range(200):
#     timmy_the_turtle.setheading(choice((0, 90, 180, 270)))
#     timmy_the_turtle.pencolor(random_color())
#     timmy_the_turtle.forward(30)


# 172 - draw a spirograph
# colormode(255)
#
#
# def random_color():
#     return randint(0, 255), randint(0, 255), randint(0, 255)
#
#
# timmy_the_turtle.speed("fastest")
#
#
# def draw_spirograph(gap_size):
#     for _ in range(360//gap_size):
#         timmy_the_turtle.pencolor(random_color())
#         timmy_the_turtle.circle(100)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading() + gap_size)
#
#
# draw_spirograph(15)

screen = Screen()
screen.exitonclick()

