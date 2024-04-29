from replit import clear
bids={}
bidding_finished= False
def find_highest_bidder(bidding_record):
    highest_bid=0
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount> highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with the bid_amount of ${highest_bid}")
while not bidding_finished:
   name=input("Enter your name: ")
   bid=int(input("Enter your bid   $"))
   bids[name]=bid
   check=input("Are ther any other bidders? Type Yes or No.\n").lower()
   if check=="no":
      bidding_finished= True
   elif check=="yes":
      clear()
    
find_highest_bidder(bidding_record=bids)

