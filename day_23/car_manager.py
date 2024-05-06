from turtle import Turtle
import random

COLORS="red orange cyan green pink blue brown purple seagreen yellow ".split()
STARTING_MOVE= 5
MOVE_INCREAMENT=1
X=-290
Y=(-250,250)


class Cars:

    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE


    def create_cars(self) :
        random_choice=random.randint(1,6)
        if random_choice==1:
            new_car=Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.speed("fastest")
            new_car.penup()
            new_car.goto(X,random.randint(-280,280))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    
    def move_cars(self):
        for caro in self.all_cars:
            caro.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREAMENT
        


   



