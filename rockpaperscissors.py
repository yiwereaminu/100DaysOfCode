import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
gameList = [rock,paper,scissors]

# computer choice
compChoice = random.randint(0,2)
# user choice

userChoice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
userChoice = int(userChoice)
print(f"Your choice: {gameList[userChoice]} computer's choice:{gameList[compChoice]}")
if userChoice == compChoice:
    print("It's a draw game")
elif userChoice == 0 and compChoice == 1:
    print("Computer wins!")
elif userChoice == 1 and compChoice == 2:
    print("COMPUTER WINS!")
elif userChoice == 2 and compChoice == 0:
    print("COMPUTER WINS!")
else:
    print("USER WINS")
