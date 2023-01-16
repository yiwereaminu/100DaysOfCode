import random
import hangman_words
import hangman_art

print(hangman_art.logo)

stages = hangman_art.stages
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)


print(chosen_word)

lives = 6

display = []
for num in range(0,len(chosen_word)):
    display.append('_')
    num +=1
print(''.join(display))
# while chosen_word != ''.join(display):
while lives !=0:
    if chosen_word == ''.join(display):
        print('You win, bravo!') 
        exit()
    guess = input("Guess a letter: ").lower()
    if guess in ''.join(display):
        print(f'You already guessed this word: {guess}')
        
    elif guess not in chosen_word:
        lives -= 1
        print(f'{guess} is not in the chosen word.')
         
    
   
    for num in range(0,len(chosen_word)):
        if chosen_word[num] == guess:
            display[num] = guess
       
    print(''.join(display))
    
    print(stages[lives])                     
    
if lives == 0:
    print(f'You lose, the chose word is: {chosen_word}')


