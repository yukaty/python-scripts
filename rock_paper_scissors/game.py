# Mini Game - Rock-Paper-Scissors

import random

# Print a welcome message
print("Welcome to Rock-Paper-Scissors!")

# The possible options
choices = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

while True:
    # Get the computer's choice
    computer_choice = random.randint(1, 3)

    # Get the user's choice
    print("================================")
    print("Enter your choice: ")
    print("1: Rock")
    print("2: Paper")
    print("3: Scissors")
    user_choice = int(input())

    # Check if the user's choice is valid
    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    # Print the choices
    print("=====")
    print("You chose: ", choices[user_choice])
    print("Computer chose: ", choices[computer_choice])
    print("=====")

    # Check who won
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 1 and computer_choice == 3:
        print("You win!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    elif user_choice == 3 and computer_choice == 2:
        print("You win!")
    else:
        print("Computer wins!")

    # Ask user if they want to play again
    print("Do you want to play again? (y/n)")
    play_again = input()

    if play_again != "y":
        print("Thanks for playing!")
        break
