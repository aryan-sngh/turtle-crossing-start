import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up,"space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if player.ycor() > 280:
        player.reset_position()
        scoreboard.increase_score()
        car_manager.levelup()

    #detect collision
    for car in car_manager.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()