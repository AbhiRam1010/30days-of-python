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
    players_card= [random.choice(cards),random.choice(cards)]
    comps_turn= [random.choice(cards),random.choice(cards)]
    if 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1)
    print(f"Player's 1st 2 cards are ; {players_card}")
    print(f"Computer's 1st card is: {comps_turn[0]} ")
    def count():
     while sum(players_card)<21:
            add_one=input("You want to pick another card: if you, press 'y' else 'n' ").lower()
            if add_one=='y':
             players_card.append(random.choice(cards))
             print(f"Player's cards are ; {players_card} ")
             while sum(comps_turn)<sum(players_card) & sum(comps_turn)<17:
                    comps_turn.append(cards)
                    print(f"computer's card{comps_turn}")
            elif add_one=='n':
                while sum(comps_turn)<sum(players_card) & sum(comps_turn)<17:
                    comps_turn.append(cards)
                    print(f"computer's card{comps_turn}") 
                if sum(comps_turn)>sum(players_card) & sum(comps_turn)<21:
                   print(f"computer's card{comps_turn}")
                   print("You loose")
                if sum(comps_turn)<sum(players_card) & sum(players_card)<21:
                   print("you won")
                   print(f"computer's card{comps_turn}")
            count()
   if sum(players_card)==21:
        print(f"player's card {players_card}")
        print(f"computer's card{comps_turn}")
        print("CONGRATULATION MF IT'S A 'BLACK JACK'")
   if sum(players_card)>21:
        print(f"player's card {players_card}")
        print(f"computer's card {comps_turn}")
        print("YOU LOOSE 'By chance'")
    count()        
    
    
       
    #    if(players2nd_card+players2nd_card+players3nd_card<21)&(players2nd_card+players2nd_card+players3nd_card<comps_turn+comps_turn2):
    #              print("YOU WON 'loose'")
    #    elif(players2nd_card+players2nd_card+players3nd_card<21)&(players2nd_card+players2nd_card+players3nd_card>comps_turn+comps_turn2):
    #              print("You Won 'ASWASTHAMA' ")
    #    elif  (players2nd_card+players2nd_card+players3nd_card>21):
    #               print("you loose greedy")
    #    elif  (players2nd_card+players2nd_card+players3nd_card==21):
    #               print("its a 'black jack'")



    #    if  (players_card+players2nd_card+players3nd_card)<21:
    #         add_two=input("You want to pick another card: if you, press 'y' else 'n' ")
    #         if add_two=='y':
    #            players4th_card=random.choice(cards)   
    #            print(f"Player's cards are ; {players_card} , {players2nd_card},{players3nd_card},{players4th_card} ")
    #            print(f"computer's 2nd card is{comps_turn2}")
    #            if(players2nd_card+players2nd_card+players3nd_card+players4th_card<21)&(players2nd_card+players2nd_card+players3nd_card+players4th_card<comps_turn+comps_turn2+comps_turn3):
    #              print("YOU WON 'loose'")
    #            elif(players2nd_card+players2nd_card+players3nd_card+players4th_card<21)&(players2nd_card+players2nd_card+players3nd_card+players4th_card>comps_turn+comps_turn2+comps_turn3):
    #              print("You Won 'ASWASTHAMA' ")
    #            elif  (players2nd_card+players2nd_card+players3nd_card+players4th_card>21):
    #               print("you loose greedy")
    #            elif  (players2nd_card+players2nd_card+players3nd_card+players4th_card==21):
    #               print("its a 'black jack'")
    #         elif add_two=='n':
    #                 print(f"comuter's cards are {comps_turn} {comps_turn2} ")
    #                 if ((comps_turn2+comps_turn<=21) &(comps_turn+comps_turn2 > players_card+players2nd_card+players3nd_card)):
    #                     print("you loose")
    #                 elif ((players_card+players2nd_card+players3nd_card<=21) &(comps_turn+comps_turn2 < players_card+players2nd_card)):  
    #                     print("You Won")
    #                 elif  (players2nd_card+players2nd_card+players3nd_card>21):
    #                     print("you loose greedy")
    #                 elif  (players2nd_card+players2nd_card+players3nd_card==21):
    #                     print("its a 'black jack'")
    #    elif (players_card+players2nd_card+players3nd_card)==21:
    #             print("YOU WON It's a 'black jack' ")
    #    elif (players2nd_card+players3nd_card+players_card)>21:
    #             print("YOU LOOSE")

        
    # elif add_one=='n':
    #     print(f"comuter's cards are {comps_turn} {comps_turn2}")
    #     if ((comps_turn2+comps_turn<=21) &(comps_turn+comps_turn2 > players_card+players2nd_card)):
    #         print("you loose")
    #     elif ((players_card+players2nd_card<=21) &(comps_turn+comps_turn2 < players_card+players2nd_card)):  
    #         print("You Won")

