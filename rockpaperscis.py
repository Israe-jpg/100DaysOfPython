import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = int(input("What do you choose ? type 0 for Rock, 1 for Paper and 2 for Scissors !\n"))
if player == 0:
    print(rock)
elif player == 1:
    print(paper)
elif  player == 2:
    print(scissors)
elif player >= 3 or player < 0:
    print("Invalid number! You lose!")
    exit()

computer = random.randint(0,2)

if computer == 0:
    print("computer Chose: \n")
    print(rock)
elif computer == 1:
    print("computer Chose: \n")
    print(paper)
elif computer == 2:
    print("computer Chose: \n") 
    print(scissors)


if player == computer:
    print("Draw") 
elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("You win!")
elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print("Computer wins!")