from turtle import  Screen 
import time
from players import Player
from car_manager import Cars
from scoreboard import Scoreboard

turtoise=Player()
car=Cars()
SCORE=Scoreboard()

screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

screen.listen()
screen.onkey(turtoise.move_turtle,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    
    for cars in car.all_cars:
      if cars.distance(turtoise)<20:
          game_is_on=False
          SCORE.game_over()
    if turtoise.is_at_finish_line():
        turtoise.goto_start()
        car.level_up()
        SCORE.increase_score()
   




screen.exitonclick()