import random
print("welcome to the number guessing game \t")
user_input=int(input("Enter a number among 1 to 100\t"))
comp_input= random.randint(1,100)
def hard():
  print("You have 5 chance ")
  global user_input
  for i in range (0,4):
    print(f'you have {4-i} chances')
    if user_input> comp_input:
      user_input=  int(input("Too high input another number \t"))
    elif user_input<comp_input:
       user_input= int(input("Too low input a higher number\t"))   
    elif user_input==comp_input:
      return    print ("You won") 
    elif user_input!=comp_input:
       print(comp_input)
       return  print ("You loose")     
def medium():
  global user_input
  print("You have 8 chances")  
  for i in range(0,7):
    print(f'you have {7-i} chances')
    if user_input> comp_input:
     user_input=int(input("Too high input another number \t"))
    elif user_input<comp_input:
      user_input=int(input("Too low input a higher number\t"))   
    elif user_input==comp_input:
        return print ("You won") 
    elif user_input!=comp_input:
        print(comp_input) 
        return print ("You loose")
def easy():        
  global user_input
  print("You have 10 chances")
  for i in range (0,9): 
    print(f'you have {9-i} chances')
    if user_input> comp_input:
       user_input = int(input("Too high input another number \t"))
    elif user_input<comp_input:
       user_input= int(input("Too low input a higher number \t"))   
    elif user_input==comp_input:
        return  print ("You won")     
    elif user_input!=comp_input:
        print(comp_input)
        return print ("You loose") 
        
game = {
    "old": hard,
    "intermidiate": medium,
    "new": easy
}
level=(input("Yor experience in this game    : 'old' : 'intermidiate' : 'new' : "))
if level=="old":
   game["old"]()
elif level=="intermidiate":
   game["intermidiate"]()
elif level=="new":
   game["new"]()
