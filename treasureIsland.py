print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
direction = input("left or right ?")
if direction ==  "left":
    print("You fell into a hole, Game over !")
elif direction == "right":
    decision = input("swim or wait ?")
    if decision == "swim":
        print("Attacked by Trout, GAME OVER !")
    elif decision == "wait":
        door = input("whoch door: blue, red or yellow ?")
        if door == "blue":
            print("Eaten by beasts, GAME OVER!")
        elif door == "red":
            print("Burned by fire, GAME OVER !")
        elif door == "yellow":
            print("You win !")
        else:
            print("GAME OVER.")
    else:
        print("GAME OVER.")
else:
    print("GAME OVER.")

