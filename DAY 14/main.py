# the higher and lower game logic
"""
the game starts with two random accounts from the game data
when you make a guess of the account with the most followers,
if you guessed correct, the score variable updates +1
the second account moves to top and a random account is 
selected and compared with it.
if you guessed wrongly, the game ends


"""
import os
from random import randint
import art
import game_data

score = 0

print(art.logo)
rand = randint(0,len(game_data.data)-1)
next_randint = randint(0,len(game_data.data)-1)
# get random question
def first_account():
    print(f"Compare A: {game_data.data[rand]['name']}, a {game_data.data[rand]['description']}, from {game_data.data[rand]['country']}")
    return game_data.data[rand]['follower_count']

def next_account():
    print(f"Compare B: {game_data.data[next_randint]['name']}, a {game_data.data[next_randint]['description']}, from {game_data.data[next_randint]['country']}")
    return game_data.data[next_randint]['follower_count']

flag = True

first_account()
print(art.vs)
next_account()

user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
while flag:
    
    if (user_answer == 'a' and first_account() > next_account()) or (user_answer=='b' and (next_account() > first_account())):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(art.logo)
        score += 1
        rand = next_randint
        next_randint = randint(0,len(game_data.data)-1)
        print(f"You're right! Current score {score}")

        first_account()
        print(art.vs)
        next_account()
        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score} ")
        flag = False

