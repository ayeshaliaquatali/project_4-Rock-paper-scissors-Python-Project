# Rock, paper, scissors Python Project
# you will work with random.choice(), if statements, and getting user input. 
# This is a great project to help you build on the fundamentals like conditionals and functions.



import random 
def lets_play():
    user_input = input("Enter the choice paper (p) , rock (r) , scissors (s) :").lower()
    if (user_input not in ["p","r","s"]):
        print("Invaild number : Enter the choice paper (p) , rock (r) , scissors (s) :")
        return
    computer_choice = random.choice(["p", "r" , "s"])
    print(f"you chose {user_input} computer chose {computer_choice} ")
    if (user_input == computer_choice):
        print("you and computer_choice are same. it's a tie")
    elif user_input== "s" and computer_choice == "p":
        print("you win the game:")    
    elif user_input== "p" and computer_choice == "r":
        print("you win the game:")    
    elif user_input== "r" and computer_choice == "s":
        print("you win the game:")
    else:
        print("you loss the game:")         
lets_play()
