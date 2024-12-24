import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ["?", "!", "/", "%", "£", "$","µ", "ù","é","&","è","ç","à","@","^","¤"] 
print("Welcome to the PyPassword Generator !")
num_letters = int(input("How many letters would you like in your password ?"))
num_symbols = int(input("How many symbols would you like in your password ?"))
num_numbers = int(input("How many numbers would you like in your password ?"))

password_elements = []

for n in range(1,num_letters + 1):
    letter = random.choice(letters)
    password_elements.append(letter)
    
for n in range(1, num_numbers + 1):
    number = random.randint(0,10)
    password_elements.append(number) 
    
for n in range(1, num_symbols + 1):
    symbol = random.choice(symbols)
    password_elements.append(symbol)

random.shuffle(password_elements)
print(*password_elements,sep='')
