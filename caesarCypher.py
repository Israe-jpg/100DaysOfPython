letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(message, shift):
    encrypted_message=[]
    for i in range(0, len(message)):
        j = letters.index(message[i]) + shift
        if j <  25:
            encrypted_message.append(letters[j])
        elif j >= 25:
            encrypted_message.append(letters[j - 26])
   
    new_message = "".join(encrypted_message)
    print(f"Here is the encoded code:{new_message}")
    go_again= input("Type 'yes' if you wanna go again, other wise type 'no':")
    if go_again == 'yes':
        cypher()
    else:
        print("bye !")

def decode(message, shift):
    decrypted_message=[]
    for i in range(0, len(message)):
        j = letters.index(message[i]) - shift
        decrypted_message.append(letters[j])
    new_message = "".join(decrypted_message)
    print(f"Here is the decoded code:{new_message}")
    go_again= input("Type 'yes' if you wanna go again, other wise type 'no':")
    if go_again == 'yes':
        cypher()
    else:
        print("bye !")
    

def cypher():
    choice = input("type 'encode' to encrypt, and 'decode' to decrypt :").lower()
    message = input("Type your message :")
    shift = int(input("Type your shift :"))
    if choice == "encode":
        encode(message,shift)
    elif choice == "decode":
        decode(message,shift)
    else:
        print("Error")

cypher()
        