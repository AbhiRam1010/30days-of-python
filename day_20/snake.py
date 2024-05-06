from turtle import Screen
from score_board import Scoreboard
from snake_game import Snake
import time
from bug import Food
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scores=Scoreboard()

game_on=True

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_lefft, "Left")
screen.onkey(snake.turn_rigght, "Right")
while game_on==True:
    

    time.sleep(.1)
    screen.update()
    snake.move()        
    scores.update_score()
    if snake.head.distance(food)<15:
       scores.increase_score()
       food.refresh()
       snake.extend()
    if snake.head.xcor()>300 or snake.head.xcor() < -300 or snake.head.ycor() < - 300 or snake.head.ycor() > 300 :
      #  game_on= False
      #  scores.reset()
      #  snake.reset()
      pass
    for number in snake.snakes[1:]:
      if snake.head.distance(number) < 10:
         # game_on=False
         scores.reset()
         snake.reset()

 
    


screen.exitonclick()