import art
import os
import random



def deal_card():
    """Returns radom card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0,len(cards)-1)]

user_cards = []
computer_cards = []

for _ in range(2):
   user_cards.append(deal_card())
   computer_cards.append(deal_card())




def calculate_score(card_list):
    """Return the sum of a list of cards"""
    if len(card_list)==2 and sum(card_list) == 21:
        return 0
    elif sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)
def drawAnotherCard(game):
    while game == True:
        draw_another_card=input("Type 'y' to get another Card and type 'n' to pass: ").lower()
        if draw_another_card == 'n':
             game = False
             break
                
        else:
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            if user_score > 21:
                # compare(calculate_score(user_cards),calculate_score(computer_cards))
                game = False
           
            
        return game

def compare(user_score, comp_score):
    if user_score == comp_score:
        print("It's a draw")
    elif user_score == 0:
        print("User wins")
    elif comp_score == 0:
        print("Computer wins")
    elif user_score > 21:
        print("Computer wins")
    elif comp_score > 21:
        print("User wins")
    elif (comp_score <= 21) and (comp_score > user_score):
        print("computer wins") 
    else:
        print("User wins")
    
user_score = calculate_score(user_cards)
comp_score = calculate_score(computer_cards)

flag = True

if user_score == 0 or comp_score == 0 or user_score > 21:
    flag =False




play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
if play == 'n':
    exit()
else:
    print(art.logo)
    while flag:
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's cards: {computer_cards[0]}")
        flag = drawAnotherCard(flag)
        

while comp_score !=0 and  comp_score < 17:
    computer_cards.append(deal_card())
    comp_score = calculate_score(computer_cards)

print(f"Computer's cards: {computer_cards}, current score: {calculate_score(computer_cards)}") 

compare(calculate_score(user_cards),calculate_score(computer_cards))