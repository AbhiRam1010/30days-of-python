from replit import clear
import randomy
def play_game():
    design=''' _     _            _      _          _    
    | | B | | L A C K  | |  J | | A C K  | |   
    | |__ | | __ _  ___| | ___  __ _  ___| | __
    | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   <| | (_| | (__|   < 
    |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\           
                    '''
    print(design)
    is_game_over=False
    user_card=[]
    computr_card=[]
    def deal_card():
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        card =random.choice(cards)
        return card
    def calculate_score(cards):
        if sum(cards)==21 and len(cards) ==2:
            return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, comp_score):
        if user_score== comp_score:
            return "draw"
        elif comp_score ==0:
            return "Loose , opponent has a black jack"    
        elif user_score > 21:
            return "You loose"
        elif comp_score > 21:
            return " opponent went over you win"
        elif user_score>comp_score:
            return "You win"
        elif user_score==0:
            return"Congrats you have a jackpot"
        else:
            return " You LOOSE"


    for n in range(2):
     user_card.append(deal_card())
     computr_card.append(deal_card())
    while not is_game_over:
        user_score=calculate_score(user_card)
        comp_score=calculate_score(computr_card)
        print(f"your cards {user_card}, your score {user_score} ")
        print(f"computer's cards {computr_card}, computer's score {comp_score} ")
        if user_score==0 or comp_score==0 or user_score>21:
         is_game_over=True   
        else:
            user_should_deal=input("Tyepe 'y' to get another card , type 'n' to pass: ")  
            if user_should_deal=='y':
                user_card.append(deal_card())
            else:
                is_game_over=True

    while comp_score !=0 and comp_score<17:
        computr_card.append(deal_card())
        comp_score = calculate_score(computr_card)
    print(f"your cards {user_card}, your score {user_score} ")
    print(f"computer's cards {computr_card}, computer's score {comp_score} ")
    print(compare(user_score,comp_score))
while input("Do you want to play black jack? Type 'y' or 'n' : ")=='y':
     clear()
     play_game()