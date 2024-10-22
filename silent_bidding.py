import os
# python clear concole function cls()
def cls():
  os.system('cls' if os.name=='nt' else 'clear')

biddings = {}

bidding = True 
highest_bid = 0
highest_bidder = None

while bidding is True:
  print("Welcome to Silent Betting")
  name = input("Enter your Name: ")
  bid = int(input("Enter your Bid: "))

  
  def add_new_bid(name, bid):
      biddings[name] = bid 

  
  add_new_bid(name, bid)

  again = input("Type Yes to bid again...").lower()
  if again == "yes":
    bidding = True
    cls()
  else:
    bidding = False

if bidding == False:
  for money in biddings:
    bids = biddings[money]
    if bid > highest_bid:
      highest_bid = bid
      highest_bidder = name
      
  print(f"The winner of Silent Bet is {highest_bidder}")
  
  

