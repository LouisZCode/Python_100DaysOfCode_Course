import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Create the player object
player = Player()

#Define controls
screen.listen()
screen.onkey(player.player_move, "Up")

#define Score
score = Scoreboard()


# define Cars:
car = CarManager()

#Game Logic
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.car_create()  # Randomly create new cars
    car.car_move()  # Move all cars


    # Collision detection with all cars
    for each_car in car.all_cars:
        if player.distance(each_car) < 20:
            player.write("GAME OVER", font=("Courier", 24, "normal"))
            game_is_on = False

        elif each_car.xcor() == -300:
            pass

    # Level up
    if player.ycor() > 280:
        score.score += 1
        score.update_level()
        player.player_restart()
        car.car_accelerate()



screen.exitonclick()