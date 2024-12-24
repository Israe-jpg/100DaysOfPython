import random

words = ["cat","dog","jerry","tom"]
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                  

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print(logo)
print(hangman[0])
word = random.choice(words)

# display word to be guessed:
display = ""
n =0
while n<len(word):
    display = display + "_"
    n +=1
display = list(display)

# lives are represented as i

i=0
while i<6 and "".join(display) != word:
    print("".join(display) )
    guess = input("Guess a letter: ")
    
    if guess in word:
        if guess in display:  # Check for repeated guess BEFORE updating display
            print(f"You already guessed {guess}")
            i += 1
            print(hangman[i])
        else:
            for x in range(len(word)):
                if word[x] == guess:
                    display[x] = guess
                    print(hangman[i])
            
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life !")
        i +=1 
        print(hangman[i])
if i == 6 and display != word:
    print("You lose !")
elif i <=6 and "".join(display) == word:
    print("You win !")






      




   

            


                



    

        
