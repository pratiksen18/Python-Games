import random

while True:
    print(".......*stone*.......\n.......*paper*......\n.....*scissors*.....")
    name = input("What is your name? ")
    print("Welcome! ", name)
    your_turn = input("Enter your turn (stone, paper, scissors): ")
    variables = ["stone", "paper", "scissors"]
    bot_turn = random.choice(variables)
    print(f"\nYou chose {your_turn}, computer chose {bot_turn}.\n")
    if your_turn.lower() == bot_turn:
        print(f"Both players selected same turn. It's a tie!")
    elif your_turn.lower() == "stone":
        if bot_turn == "scissors":
            print("Congratulations! stone smashes scissors! You win!")
        else:
            print("Oops! Paper covers stone! You lose.")
    elif your_turn.lower() == "paper":
        if bot_turn == "stone":
            print("Congratulations! Paper covers stone! You win!")
        else:
            print("Oops! Scissors cuts paper! You lose.")
    elif your_turn.lower() == "scissors":
        if bot_turn == "paper":
            print("Congratulations! Scissors cuts paper! You win!")
        else:
            print("Oops! stone smashes scissors! You lose.")
    else:
        print("Something went wrong...!\nthis is an invalid input. Please check your spelling!")

    again = input("Play again? (yes/no): ")
    if again.lower() != "yes":
        break