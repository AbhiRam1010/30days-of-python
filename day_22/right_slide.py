from turtle import Turtle , Screen

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)

class paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.width=20
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        self.color("lime")
        self.speed("fast")
    

        # self.showturtle()

    def go_up(self):
        new_y= self.ycor()+20
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y= self.ycor()-20
        self.goto(self.xcor(),new_y)

    
