# Heads or Tails
from random import choice # function that randomly chooses from a list
user_exit = ""

while True:
    print("Welcome to our Heads or Tails Game!")

    while True:
        user_input = input("Please choose heads or tails: \nUser's Choice: ")
        user_input = user_input.lower() # makes everything lowercased

    # "in" operator is the membership checker
        if user_input in {"heads", "tails", "head", "tail"}:
            # user_input was valid
            break # exit a looping structure
        else:
            print("please type in heads or tails. :)")
    #end of while

    flip_result = choice(["heads", "tails"])
    print(f"The computer flipped {flip_result}")
    # and and or combines conditions, not values
    if user_input in {"heads", "head"} and flip_result == "heads":
        print("The user guessed correctly")
    elif user_input in {"tails", "tail"} and flip_result == "tails":
        print("The user guessed correctly")
    else:
        print("You lose...")

    if user_exit != "i want to do this for the rest of my life":
        user_exit = input("Play Again? (yes or no): ")
        user_exit = user_exit.lower()
        if user_exit in {"no", "no thanks", "fuck off", "never again", "i hate flipping coins"}:
            print("Closing Game...")
            break
        elif user_exit in {"yes", "yes please", "i love flipping coins", "i want to do this for the rest of my life"}:
            print("Relaunching Game...")
        else:
            print("Invalid input, closing game")

    