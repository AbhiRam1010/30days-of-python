from turtle import Turtle
from right_slide import paddle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.color("lime")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.y_move=10
        self.x_move=10
        self.move_speed=0.1
     
    

    def move(self):
        self.speed("fastest")
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    
    def bounce_y(self):
            self.y_move*=-1
            # self.move_speed*=-1

    def bounce_x(self):
           self.x_move*=-1
           self.move_speed*=0.9
    
    def restart(self):
         self.move_speed=0.1
         self.goto(0,0)
         


