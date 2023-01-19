import art
import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
score = 0
for i in range(0,len(cards)):
    score += cards[i]
    
print(score)

def calculate_score(cards):
    score = 0
    for i in range(0,len(cards)):
        score += cards[i]
        
    return score

def deal_card():
    return cards[random.randint(0,len(cards)-1)]
    



cont_play = True
while cont_play:
    user_cards = []
    computer_cards = []
    play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if play == 'y':
        user_cards.append(deal_card)
        user_cards.append(deal_card)
        computer_cards.append(deal_card)

        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's cards: {computer_cards}, current score: {calculate_score(computer_cards)}")
        print("Type 'y' to get another Card and type 'n' to pass: ").lower()
    else:
        exit()