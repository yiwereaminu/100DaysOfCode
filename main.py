# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# name1 = name1.lower()
# name2 = name2.lower()
# name = name1 + name2
# countT = name.count('t')
# countR =name.count('r')
# countU = name.count('u')
# countE = name.count('e')
# countL = name.count('l')
# countO = name.count('o')
# countV = name.count('v')
# countEl = name.count('e')

# trueTotal = countT+countR+countU+countE
# loveTotal = countL+countO+countV+countEl

# loveScore = str(trueTotal)+ str(loveTotal)

# print(loveScore)

name = 'hayjak'
guess = input('guess a letter')

if guess not in name:
    print('you lose')