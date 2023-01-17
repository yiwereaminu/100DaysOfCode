import art
import os

bid = True

blind_auction = {}
while bid:
    print(art.logo)
    print("Welcome to the secret aution program.")
    name = input("What's your name: ")
    bid_amount = int(input("How much do you want to bid: $"))
    blind_auction[name] = bid_amount
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if more_bidders == 'no':
        os.system('cls' if os.name == 'nt' else 'clear')
        bid = False
    else:
       os.system('cls' if os.name == 'nt' else 'clear')

highest_bid = 0
name_of_highest_bidder = ''      
for key in blind_auction:
    if blind_auction[key] > highest_bid:
        highest_bid = blind_auction[key]
        name_of_highest_bidder = key
print(f'the highest bidder is {name_of_highest_bidder.capitalize()} with a total bid of: ${highest_bid} ')