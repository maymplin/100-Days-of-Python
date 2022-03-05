# https://pypi.org/project/colorgram.py/

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst_painting.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

# https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen, colormode
from random import choice

color_list = [(212, 149, 95), (215, 80, 62), (47, 94, 142), (231, 218, 92), (148, 66, 91), (22, 27, 40), (155, 73, 60), (122, 167, 195), (40, 22, 29), (39, 19, 15), (209, 70, 89), (192, 140, 159), (39, 131, 91), (125, 179, 141), (75, 164, 96), (229, 169, 183), (15, 31, 22), (51, 55, 102), (233, 220, 12), (159, 177, 54), (99, 44, 63), (35, 164, 196), (234, 171, 162), (105, 44, 39), (164, 209, 187), (151, 206, 220)]

colormode(255)
tim = Turtle()
tim.speed("fastest")

tim.hideturtle()
tim.penup()
tim.setposition(-100, -150)

for x in range(10):
    for y in range(10):
        tim.dot(20, choice(color_list))
        tim.penup()
        tim.forward(50)
    tim.setposition(-100, tim.ycor() + 50)

screen = Screen()
screen.exitonclick()