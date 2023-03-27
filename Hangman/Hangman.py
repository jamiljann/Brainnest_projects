'''
The hangman game is a word guessing game where the player is given a word and has to guess the letters that make up the word. 
The player is given a certain number of tries (no more than 6 wrong guesses are allowed) to guess the correct letters before the game is over.
'''
# Output
'''
You have 6 tries left.                                                                                                                                           
Used letters:                                                                                                                                                    
Word: _ _ _ _                                                                                                                                                    
Guess a letter: a 

You have 6 tries left.                                                                                                                                           
Used letters: a                                                                                                                                                  
Word: _ a _ a                                                                                                                                                    
Guess a letter: j    

You have 6 tries left.                                                                                                                                           
Used letters: j a                                                                                                                                                
Word: j a _ a                                                                                                                                                    
Guess a letter: v                                                                                                                                                
You guessed the word java !
'''
import random
  
# select a random value from the list to make a guess
random_words = ['python', 'program', 'java', 'c++']
selected_word = random.choice(random_words)
# The user's guest
selected_answer = []
counter = 0
Used_letters =''
#initialize a list of input leters
for chars in selected_word:
    selected_answer.append('_ ')
#let user to input a char
while counter < 6:
    count = -1
    word =''
    
    print("\n")
    print('You have', 5-counter+1 ,'tries left.' )
    print('Used letters:', Used_letters)
    for item in selected_answer:
        word += item
    print('Word:', word)
    word =''
    
    input_char = input('Guess a letter:')
    while len(input_char) > 1:
        print ("Only one character you should enter. Try again. ")
        input_char = input('Guess a letter:')
    Used_letters = Used_letters + input_char + ' '
    if input_char not in selected_word:
        counter += 1
    for item in selected_word:
        count +=1
        if item == input_char:
            selected_answer[count] = input_char
    for item in selected_answer:
        word += item
    if '_' not in word: 
        print('You guessed the word:', word, '!')
        break 
    
if '_' in word: 
    print('You missed the word:', selected_word)
    


