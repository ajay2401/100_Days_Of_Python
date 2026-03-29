import random

user_input = int(input('''\nPlease enter 
0 for Rock
1 for Paper
2 for Scissors\n\n'''))

default_values = ["Rock","Paper","Scissors"]

computer_choice = random.choice(default_values)

if user_input >= 0 and user_input <=2:
    if (user_input == 0 and computer_choice == "Paper") or (user_input == 1 and computer_choice == "Scissors") or (user_input == 2 and computer_choice == "Rock"):
        
        print(f"\nThe computer chose: {computer_choice}\n")
        print("Game Over..You Lose")
    
    elif (user_input == 0 and computer_choice == "Rock") or (user_input == 1 and computer_choice == "Paper") or (user_input == 2 and computer_choice == "Scissors"):
        
        print(f"\nThe computer chose: {computer_choice}\n")
        print("Game Draw..Wanna go again?")
        
    else:
    
        print(f"\nThe computer chose: {computer_choice}\n")
        print("Game Over..You Won")
else:
    print("Enter proper values")
