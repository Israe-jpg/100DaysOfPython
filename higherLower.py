import random
import os

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    }
]




# compare A and B
def compare(a, b):
    if a >  b:
        return 'a'
    elif a < b:
        return 'b'



# play game function
def play():
    #tracking game
    game_over = False
    score = 0
    while game_over == False:

        #generating the A and B
        picks = random.sample(data, 2)
        A = picks[0]['name']
        B = picks[1]['name']
        a = picks[0]['follower_count']
        b = picks[1]['follower_count']
        
        #input
        print(logo)
        print(f"compare A: {A}, {picks[0]['description']} from {picks[0]['country']}.")
        print(vs)
        print(f"against B: {B}, {picks[1]['description']} from {picks[1]['country']}.")
        choice = input("Who has more followers ? Type 'A' or 'B': ").lower()
        
        if compare(a, b) == choice:
            score += 1  
            os.system('cls||clear')         
            print(f"That's right, Your current score is {score}")
            
        else:
            print(f"That's wrong, game over, your final score is {score}")
            break
            os.system('cls||clear')



play()


