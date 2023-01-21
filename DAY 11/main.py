import art
import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
score = 0

def calculate_score(cards):
    score = 0
    for i in range(0,len(cards)):
        score += cards[i]
    if len(cards) == 2 and sum(cards) ==21:
        return 0
    elif 11 in cards and score >= 21:
        cards.remove(11)
        cards.append(1)


        
    return score


def deal_card():
    return cards[random.randint(0,len(cards)-1)]

def compare(user_score,computer_score):
    """a function that take the return value of the calculate_score function and compare the score of the user and computer"""
    if user_score == computer_score:
        print("Game over! It's a draw")
    elif user_score==0:
            print("Game over! User wins")
    elif computer_score==0:
            print("Game over! User Loses")
    elif user_score > 21:
            print("Game over! User Loses")
    elif computer_score > 21:
            print("Game over! Computer Loses")
    elif (computer_score<=21) and (computer_score > user_score):
            print("Game over! Computer wins")      
    else:
        print("Game Over! user wins.")

             

cont_play = True
while cont_play:
    user_cards = []
    computer_cards = []
    play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower()
    if play == 'y':
        user_cards.append(deal_card())
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        computer_cards.append(deal_card())
        # compare(calculate_score(user_cards),calculate_score(computer_cards))
        if calculate_score(user_cards)==0:
            print("Game over! User wins")
            cont_play = False
        elif calculate_score(computer_cards)==0:
            print("Game over! Computer wins")
            cont_play = False
            
        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's cards: {computer_cards[0]}")
        deal_again=input("Type 'y' to get another Card and type 'n' to pass: ").lower()
        draw_again = True
        while draw_again:
            if deal_again == 'n':
                if calculate_score(computer_cards) < 17:
                    computer_cards.append(deal_card())
                    calculate_score(computer_cards)
                    print(f"Computer's cards: {computer_cards}, current score: {calculate_score(computer_cards)}") 
                compare(calculate_score(user_cards),calculate_score(computer_cards))

                draw_again = False
                deal_again = False
                exit()
            if deal_again == 'y':
                user_cards.append(deal_card())
                calculate_score(user_cards)
                if calculate_score(user_cards) > 21:
                    print("Game over! Computer wins")
                    draw_again = False
                    cont_play = False
                    exit()
                elif calculate_score(user_cards) < 21:
                    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
                    print(f"Computer's cards: {computer_cards}, current score: {calculate_score(computer_cards)}")                  
    else:
        cont_play = False

