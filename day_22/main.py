from turtle import  Screen,Turtle
from right_slide import paddle
from pong import Ball
import time
from scoreboard import Score


screen=Screen()
screen.tracer(0)
screen.setup(800,600)
r_paddle=paddle((350,0))
l_paddle=paddle((-350,0))
ping_pong=Ball()
scores=Score()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_on=True

while game_on:
 time.sleep(ping_pong.move_speed)
 screen.update()
 ping_pong.move()
 if ping_pong.ycor()>280 or ping_pong.ycor()<-280:
     ping_pong.bounce_y()
 if ping_pong.distance(r_paddle)<50 and ping_pong.xcor()>330:
     ping_pong.bounce_x()
 if ping_pong.distance(l_paddle)<50 and ping_pong.xcor()<-330:
     ping_pong.bounce_x()
 if ping_pong.xcor()>350 : 
    ping_pong.restart()
    ping_pong.bounce_x()
    scores.l_point()

 if ping_pong.xcor()<-350:
    ping_pong.restart()
    ping_pong.bounce_x()
    scores.r_point()

      
      

    

screen.exitonclick()


