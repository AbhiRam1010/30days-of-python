from turtle import Turtle, Screen
import random
is_race_on=False
screen=Screen()
screen.setup(height=800,width=700)
user_bid= screen.textinput(title="Make your bet",prompt="Which turtlr will win the race?  Enter a color: ")
colors=("red orange yellow green blue purple").split()
y_position=[0,40,80,-40,-80,90]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtles =Turtle(shape="turtle")
    new_turtles.color(colors[turtle_index])
    new_turtles.penup()
    new_turtles.goto(x=-320,y=y_position[turtle_index])
    all_turtles.append(new_turtles)
if user_bid:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
     if turtles.xcor() > 350:
        is_race_on=False
        winning_color= turtles.pencolor()
        if winning_color== user_bid:
           print(f'congratulation you won you choose {user_bid} and winner is {winning_color}')
        else:
           print(f'fuckoff you lost you choose {user_bid} and winner is {winning_color}')
    
     rand_distance=random.randint(0,10)
     turtles.forward(rand_distance)


screen.exitonclick


