# -*- coding: utf-8 -*-
"""
Day 16: Intermediate - Object Oriented Programming (OOP)
https://docs.python.org/3/library/turtle.html
"""

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red", "green")

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
