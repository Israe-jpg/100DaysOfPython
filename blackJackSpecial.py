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
cards = [11 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]

# dealing a card
def deal_card(card):
    card = random.choice(cards)
    return card



#calculate score function
def calculate_score(cards):
    
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) >= 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Compare scores
def compare(player_score, computer_score):
    # First check for blackjacks (0)
    if computer_score == player_score == 0:
        return print("BlackJack, but it's a draw :(")
    elif player_score == 0:
        return print("BlackJack! You win!")
    elif computer_score == 0:
        return print("BlackJack! Computer wins!")
    
    # Then check for busts (over 21)
    if player_score > 21:
        return print("You went overboard, computer wins!")
    elif computer_score > 21:
        return print("Computer went overboard, you win!")
    
    # Finally compare regular scores
    if player_score == computer_score:
        return print("It's a draw!")
    elif player_score > computer_score:
        return print("You win!")
    else:  # computer_score > player_score
        return print("Computer wins!")

# playing game 
def play_game():
    print(logo)
    while True:
        # Initialize new round
        player_cards = [deal_card(cards), deal_card(cards)]
        computer_cards = [deal_card(cards), deal_card(cards)]
        is_game_over = False

        # Computer's initial moves
        computer_score = calculate_score(computer_cards)
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card(cards))
            computer_score = calculate_score(computer_cards)

        # Player's turn
        while not is_game_over:
            player_score = calculate_score(player_cards)
            print(f"Your cards are {player_cards}, and your score is {player_score}")
            print(f"Computer's first card is {computer_cards[0]}")
            
            # Check for instant win/lose conditions
            if computer_score == 0 or player_score == 0 or player_score > 21:
                break
            
            # Player decision
            if input("If you wanna hit type 'y', if you wanna stand type 'n': ") == 'y':
                player_cards.append(deal_card(cards))
            else:
                break

        # Calculate final scores
        player_score = calculate_score(player_cards)
        
        # Show final results
        print(f"Your final cards are {player_cards}, and final score is: {player_score}")
        print(f"Computer's final cards are {computer_cards}, and final score is: {computer_score}")
        compare(player_score, computer_score)

        # Ask to play again
        if input("Do you wanna play again, 'y' if yes and 'n' if no: ").lower() != 'y':
            break
        os.system('cls||clear')
        print(logo)

play_game()
    




    
