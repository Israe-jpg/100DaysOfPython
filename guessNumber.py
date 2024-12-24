import random
import os



#compare
def compare(number, guess):
    if number == guess:
        return 0
    if number < guess:
        return print("too high")
    else:
        return print("too low")


 #play
def play():
    # generate a number between 1 ans 100
    number = random.randint(1, 100)

# Choose game difficulty
    print("I'm guessing a number between 1 and 100 ")
    mode = input("Choose game difficulty: easy or hard ? ")
    

    #assigning the mode to the guess
    guess_number = 0
    if mode == "easy":
        guess_number = 10
    elif mode == "hard":
        guess_number = 5
    else:
        n = 0
        for n in range(2):
            mode = input("error in your message.Please choose game difficulty: easy or hard ? ")
            n += 1
            if mode in ["easy", "hard"]:
                guess_number = 10 if mode == "easy" else 5
                break
        else:
            print("Too many invalid attempts. Exiting the game.")
            return  
            
       


   
    guess = int(input("make a guess: "))
    i = 1

    while i < guess_number :
        result = compare(number, guess)
        if result == 0:
            print("That's right !")
            break
        guess = int(input(f"You only have {guess_number - i} guess left, guess again : "))
        i += 1
    if i >= guess_number:
        if guess == number:
            print("That's right !")
            
        else:
            print("You have run out of guesses, you lose !")
            
play()
if input("do you wanna play again ? y or n: " ) == 'y':
    os.system('cls||clear')
    
    play()
else:
    os.system('cls||clear')