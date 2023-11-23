# Create a game logic "Rock, Paper, Scissors" using Python; At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent. By the end of each round, the player can choose whether to play again. Display the player's score at the end of the game. The game must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
# The game should inform the player whether the player won, lost, or tied with the opponent. Choose to continue playing.

import random

options = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    player_choice = input("Choose rock, paper, or scissors: ")
    computer_choice = random.choice(options)
    print("You chose: " + player_choice)
    print("The computer chose: " + computer_choice)

    # The game should inform the player if the option entered by the player is invalid.
    if player_choice not in options:
        print("Invalid input. Try again.")
        continue

    if player_choice == computer_choice:
        print("You tied!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        player_score += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
        player_score += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print("Player Score: " + str(player_score))
    print("Computer Score: " + str(computer_score))

    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break

print("Final Score: ")
print("Player Score: " + str(player_score))
print("Computer Score: " + str(computer_score))
