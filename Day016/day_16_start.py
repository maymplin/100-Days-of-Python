# -*- coding: utf-8 -*-
"""
Day 16: Intermediate - Object Oriented Programming (OOP)
https://docs.python.org/3/library/turtle.html
"""

# from turtle import Turtle, Screen
import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("green")
print(timmy.position())
timmy.forward(300)
print(timmy.position())

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
