# from turtle import Turtle,Screen

# tim = Turtle()
# screen= Screen()

# def move_forward():
#    tim.forward(10) 

   
   
   
# screen.listen()
# screen.onkey(key="space",fun= move_forward)

    
    
# screen.exitonclick()

print("Welcome you to the calculator")
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
n1=int(input("Enter a number:  "))
n2=int(input("Enter another number: "))
do=input("Enter a operation: ") 
def calculator(n1,n2,do):
    return do(n1,n2)

print(calculator(n1,n2,do))



