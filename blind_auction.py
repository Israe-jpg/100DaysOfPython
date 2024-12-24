import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program !")
bidders = []
name = input("What is your name? : ")
bid = int(input("What is your bid? : "))


def add_bid(name,bid):
    bidders.append({
        'name' : name,
        'bid' : bid
    })
    other_bidder = input("Are there any other bidders ? yes or no :")
    if other_bidder == "yes":
        os.system('cls||clear')
        name = input("What is your name? : ")
        bid = int(input("What is your bid? :$"))
        add_bid(name, bid)
    else:
        highest_bid = 0
        highest_bidder = ""
        for bidder in bidders:
            if bidder['bid'] > highest_bid:
                highest_bid = bidder['bid']
                highest_bidder = bidder['name']
        print(f"The highest bidder is {highest_bidder}, with a bid of {highest_bid}$")
        

add_bid(name, bid)






