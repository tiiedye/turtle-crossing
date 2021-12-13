import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.go_up, "Up")

game_is_on = True
loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if loop >= 6:
        car_manager.create_car()
        loop = 0
    car_manager.move_car()
    loop += 1

    # Detect car collision
    for car in car_manager.all_cars:
        if turtle.distance(car) < 20:
            score.game_over()
            game_is_on = False

    # Detect if turtle reaches finish line
    if turtle.finish_line_reached():
        score.increase_level()
        car_manager.increase_car_speed()

# All code before exit
screen.exitonclick()
