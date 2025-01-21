from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = -5
MOVE_INCREMENT = -5

class CarManager:

    def __init__(self):
        self.all_cars = []  # List to store all car objects
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_create(self):
        """Randomly create a new car."""
        chance = random.randint(1, 6)  # Adjust chance as needed
        if chance == 1 or chance == 2:  # Only create a car 1 in 6 times
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randint(-250, 250))
            self.all_cars.append(new_car)  # Add new car to the list

    def car_move(self):
        """Move all cars in the list."""
        for car in self.all_cars:
            car.setx(car.xcor() + self.car_speed)

    def car_accelerate(self):
        """Increase the speed of all cars."""
        self.car_speed += MOVE_INCREMENT




