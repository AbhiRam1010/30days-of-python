import random
print("'WELCOME TO THE STONE PAPER SIZOR GAME'")
box=["stone","paper","sizor"]
comp_turn = random.randint(0,2)
player_turn= int(input("enter a number for (0=stone , 1=paper, 2=sizor) :-  "))
print(f"you choose-{box[player_turn]}")
print(f"computer choose-{box[comp_turn]}")
if (comp_turn==1) & (player_turn==0):
    print("YOU Lose!!!")
elif(comp_turn==1) & (player_turn==2):
    print("YOU WON!!!")
if (comp_turn==0) & (player_turn==1):
    print("YOU WON!!!")
elif(comp_turn==0) & (player_turn==2):
    print("YOU LOSE")
if (comp_turn==2) & (player_turn==1):
    print("YOU LOSE")
elif(comp_turn==2) & (player_turn==0):
    print("YOU WON!!!")
if(comp_turn==player_turn):
   print("It's a DRAW")
elif(player_turn>=3 & player_turn<0) : 
   print("WRONG INPUT READ THE COMMAND FIRST") 
