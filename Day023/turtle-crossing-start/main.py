# someone else's example: https://github.com/Lukas-Lelonek/Cross_the_Road

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

CREATE_CAR_CHANCE = 5

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

loop = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(0, CREATE_CAR_CHANCE) == CREATE_CAR_CHANCE:
        car_manager.add_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.is_game_over()
            game_is_on = False


    # Detect successful crossing
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start_line()
        car_manager.level_up()


screen.exitonclick()
