from turtle import Turtle,Screen
# print("Welcomr to Etch a scetch program")
timm=Turtle()
timm.shape("turtle")
screen= Screen()
def move_forward():
    timm.forward(30)
def turn_left():
    timm.lt(10)
def turn_right():
    timm.rt(10)
def move_backward():
    timm.backward(30)
def clear():
    timm.penup()
    timm.clear()
    timm.home()
    timm.pendown()
screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")

screen.exitonclick()