import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
        
print(logo)
cards = [11 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]
game_on = True

# generating the first two cards
computer_cards = []
player_cards = []

computer_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))
player_cards.append(random.choice(cards))
player_cards.append(random.choice(cards))

# computer cards control
computer_score = sum(computer_cards)

while computer_score < 17:
    computer_cards.append(random.choice(cards))
    computer_score = sum(computer_cards)

# calculate players score
player_score = sum(player_cards)

# function to update
def update():
    global player_score
    player_score = sum(player_cards)
    print(f"Your cards : {player_cards}, current score = {player_score}")
    print(f"Computer's first card is: {computer_cards[0]}")
    




while game_on == True:
    update()
    while player_score < 21:
        deal = input("type 'y' to get another card, and type 'n' to pass: ")
        if deal == "y":
            player_cards.append(random.choice(cards))
            update()
            if player_score > 21:
                print("Bust! You went over 21!")
                game_on = False
                break
        elif deal == "n":
            game_on = False
            break
            
while game_on == False:
    print(f"Your final hand is {player_cards}, and final score is : {player_score}")
    print(f"Computer's final hand is: {computer_cards}, and final score is : {computer_score}")
    if computer_score == player_score:
        print("draw")
    elif player_score < computer_score <= 21:
        print("computer wins")
    elif computer_score < player_score <= 21:
        print("You win")
    elif computer_score > 21 and player_score <= 21:
        print("computer went overboard ! You win")
    elif player_score > 21 and computer_score <= 21:
        print("oops, u went over 21, you lose")
    
        
    else:
        break
    break
    
    


    

