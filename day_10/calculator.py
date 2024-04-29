from replit import clear
from art import logo
print(logo)
print("Welcome you to the calculator")
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
operators ={
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide
            }    


def calculator():
    num1=float(input("Enter the first number: "))    
    for operation in operators:
        print(operation)
    _continue= True
    while _continue== True:
        operation_symbol= input("Pick an operator from te line above: ")
        num2=float(input("Enter the second number: "))
        calculation_function = operators[operation_symbol]
        answer= calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        again=input("want to calculate with th answer :  type 'yes' or 'no' ").lower()
        if again=="yes":
            num1=answer
            _continue=True
        else:
            _continue=False
            clear()
            calculator()
            
calculator()

    # operation_symbol=input("Enter an other operator:   ")
    # num3=int(input("Enter another number:  "))
    # calculation_function=operators[operation_symbol]
    # answer2 = calculation_function(answer,num3)
    # print(f"{answer} {operation_symbol} {num3} = {answer2}")

