from random import choice
user_placement = 1
print("Welcome to Snakes and Ladders!")
while True: 
    print(f"You are currently placed at square {user_placement}")
    
    while True:
        user_roll = int(input("Enter a roll amount (2-12): "))
        if user_roll in {0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}:
            user_placement += user_roll
            break
        else:
            print("Invalid Number, Try Again!")
        
    
    if user_placement == 9:
        print("Landed on a ladder! Move up!")
        user_placement += 25
    elif user_placement == 40:
        print("Landed on a ladder! Move up!")
        user_placement += 24
    elif user_placement == 67:
        print("Landed on a ladder! Move up!")
        user_placement += 19
    elif user_placement == 54:
        print("Landed on a snake! Move down!")
        user_placement -= 35
    elif user_placement == 90:
        print("Landed on a snake! Move down!")
        user_placement -= 42
    elif user_placement == 99:
        print("Landed on a snake! Move down!")
        user_placement -= 22
    elif user_placement > 100:
        print("Too high! Didn't move!")
        user_placement -= user_roll
    elif user_placement == 100:
        print("GG! You win!")
        user_exit = input("Would you like to play again?: ")
        if user_exit == "no":
            break
        else:
            user_placement = 1
            print("Welcome to Snakes and Ladders!")
    if user_roll == 0:
            print("Exitting game...")
            break

    

