import random
design=''' _     _            _      _          _    
| | B | | L A C K  | |  J | | A C K  | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\           
                '''
print(design)
from replit import clear
start=input("Do you wan't to play the game- To start press 'y' else 'n' ").lower()
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
if start=='y':
    players_card= random.choice(cards)
    players2nd_card=random.choice(cards)
    comps_turn= random.choice(cards)
    comps_turn2= random.choice(cards)
    comps_turn3= random.choice(cards)

    print(f"Player's 1st 2 cards are ; {players_card} , {players2nd_card} ")
    print(f"Computer's 1st card: {comps_turn} ")
    add_one=input("You want to pick another card: if you, press 'y' else 'n' ")
    if add_one=='y':
       players3nd_card=random.choice(cards)
       print(f"Player's cards are ; {players_card} , {players2nd_card},{players3nd_card} ")
       print(f"computer's 2nd card is{comps_turn2}")
    #    if(players2nd_card+players2nd_card+players3nd_card<21)&(players2nd_card+players2nd_card+players3nd_card<comps_turn+comps_turn2):
    #              print("YOU WON 'loose'")
    #    elif(players2nd_card+players2nd_card+players3nd_card<21)&(players2nd_card+players2nd_card+players3nd_card>comps_turn+comps_turn2):
    #              print("You Won 'ASWASTHAMA' ")
    #    elif  (players2nd_card+players2nd_card+players3nd_card>21):
    #               print("you loose greedy")
    #    elif  (players2nd_card+players2nd_card+players3nd_card==21):
    #               print("its a 'black jack'")
       if  (players_card+players2nd_card+players3nd_card)<21:
            add_two=input("You want to pick another card: if you, press 'y' else 'n' ")
            if add_two=='y':
               players4th_card=random.choice(cards)   
               print(f"Player's cards are ; {players_card} , {players2nd_card},{players3nd_card},{players4th_card} ")
               print(f"computer's 2nd card is{comps_turn2}")
               if(players2nd_card+players2nd_card+players3nd_card+players4th_card<21)&(players2nd_card+players2nd_card+players3nd_card+players4th_card<comps_turn+comps_turn2+comps_turn3):
                 print("YOU WON 'loose'")
               elif(players2nd_card+players2nd_card+players3nd_card+players4th_card<21)&(players2nd_card+players2nd_card+players3nd_card+players4th_card>comps_turn+comps_turn2+comps_turn3):
                 print("You Won 'ASWASTHAMA' ")
               elif  (players2nd_card+players2nd_card+players3nd_card+players4th_card>21):
                  print("you loose greedy")
               elif  (players2nd_card+players2nd_card+players3nd_card+players4th_card==21):
                  print("its a 'black jack'")
            elif add_two=='n':
                    print(f"comuter's cards are {comps_turn} {comps_turn2} ")
                    if ((comps_turn2+comps_turn<=21) &(comps_turn+comps_turn2 > players_card+players2nd_card+players3nd_card)):
                        print("you loose")
                    elif ((players_card+players2nd_card+players3nd_card<=21) &(comps_turn+comps_turn2 < players_card+players2nd_card)):  
                        print("You Won")
                    elif  (players2nd_card+players2nd_card+players3nd_card>21):
                        print("you loose greedy")
                    elif  (players2nd_card+players2nd_card+players3nd_card==21):
                        print("its a 'black jack'")
       elif (players_card+players2nd_card+players3nd_card)==21:
                print("YOU WON It's a 'black jack' ")
       elif (players2nd_card+players3nd_card+players_card)>21:
                print("YOU LOOSE")

        
    elif add_one=='n':
        print(f"comuter's cards are {comps_turn} {comps_turn2}")
        if ((comps_turn2+comps_turn<=21) &(comps_turn+comps_turn2 > players_card+players2nd_card)):
            print("you loose")
        elif ((players_card+players2nd_card<=21) &(comps_turn+comps_turn2 < players_card+players2nd_card)):  
            print("You Won")

