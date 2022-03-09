from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        self.place_car(car)
        self.cars.append(car)

    def place_car(self, car):
        random_y = random.randint(-250, 250)
        car.goto(300, random_y)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT*0.2
