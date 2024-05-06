from turtle import Turtle
starting_position=[(0,0),(-10,0),(-20,0)]
move_distance=10
up=90
down=270
right=0
left=180
class Snake:
    def __init__(self):
        self.snakes=[]
        self.create_snake()
        self.head=self.snakes[0]
    def create_snake(self):
        for position in starting_position: 
           self.add_snakes(position)

    def add_snakes(self,position):
            tommy= Turtle()
            tommy.speed("fastest")
            tommy.penup()
            tommy.shape("square")
            # tommy.pensize(10)
            tommy.goto(position)
            tommy.color("blue")
            self.snakes.append(tommy)
    def reset(self):
        for x in self.snakes:
           x.goto(1900,1900)
        self.snakes.clear()
        self.create_snake()
        self.head=self.snakes[0]
    def extend(self):
        self.add_snakes(self.snakes[-1].position())

    def move(self):
        for turtles in range(len(self.snakes)-1,0,-1):
            new_x=self.snakes[turtles-1].xcor()
            new_y=self.snakes[turtles-1].ycor()
            self.snakes[turtles].goto(new_x,new_y)
        self.head.forward(move_distance)
    
    def turn_up(self):
        if self.head.heading()!= down:
         self.head.setheading(up)
    def turn_rigght(self):
        if self.head.heading()!=left:
         self.head.setheading(right)
    def turn_down(self):
        if self.head.heading()!=up:
         self.head.setheading(down)
    def turn_lefft(self):
        if self.head.heading()!=right:
         self.head.setheading(left)