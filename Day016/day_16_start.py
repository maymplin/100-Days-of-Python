# -*- coding: utf-8 -*-
"""
Day 16: Intermediate - Object Oriented Programming (OOP)
https://docs.python.org/3/library/turtle.html
https://pypi.org/project/prettytable/
https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
https://pypi.org/
"""

# from turtle import Turtle, Screen
import turtle
import prettytable

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("green")
print(timmy.position())
timmy.forward(300)
print(timmy.position())

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
