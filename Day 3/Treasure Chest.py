print("\n" + '''***Welcome to the Treasure Chest Island***
   Your mission is to find the treasure''')

user_input = input("Enter whether you want to go Left or Right?\n").lower()
game_over = "GAME OVER!! YOU LOST :("

if user_input == "left":
    user_input = input("\nSwim or Wait?\n").lower()
    if user_input == "wait":
        user_input = input('''\n Which door of these would you like to wait in
            1.) Red
            2.) Green
            3.) Blue\n''')
        if user_input.upper() == "GREEN":
            print("YOU WIN!!\n")
        else: 
            print("\n"+game_over)
    else: 
        print("\n"+game_over)
else: 
    print("\n"+game_over)
            
            
        

