from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

scoreboard = Scoreboard()

is_game_on = True
while is_game_on:
    time.sleep(.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()

    # Detect finish line
    if player.is_at_finish_line():
        player.goto_start()
        scoreboard.update_score()
        car_manager.level_up()

screen.exitonclick()