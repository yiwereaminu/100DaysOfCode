import random


def difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard' : ").lower()
    attempts = 0
    if level == 'easy':
        attempts = 10
    elif level == 'hard':
        attempts = 5
    # print(f"You have {attempts} attempts remaining to guess the number.")
    return attempts
def compare():
    attempts = difficulty()
    random_number = random.randint(1,100)
    flag = True
    user_guess = int(input("Make a guess: "))
    attempts -= 1
    while attempts >= 0 and flag:
        if random_number == user_guess:
            print(f'You got it the answer was {random_number}')
            flag = False
        elif attempts == 0:
            print("You've run out of guesses, you lose!")
            flag = False
        elif user_guess > random_number:
            print(f"Too high\nGuess again\nYou have {attempts} attempts left")
            user_guess = int(input("Make a guess: "))
        elif user_guess < random_number:
            print(f"Too low\nGuess again\nYou have {attempts} attempts left")
            user_guess = int(input("Make a guess: "))
        attempts -= 1 
        
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
# attempts = difficulty()
compare()



  