# -*- coding: utf-8 -*-
"""
Day 16: Intermediate - Object Oriented Programming (OOP)
https://docs.python.org/3/library/turtle.html
https://pypi.org/project/prettytable/
https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
https://pypi.org/
"""

# # from turtle import Turtle, Screen
# import turtle
#
# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# print(timmy.position())
# timmy.forward(300)
# print(timmy.position())
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()  # create the object table
table.add_column("Pokemon Name", ["Chespin", "Fennekin", "Froakie"])
table.add_column("Type", ["Grass", "Fire", "Water"])
table.align = "l"
print(table)
