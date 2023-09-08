# We will write a rock paper scissors game in class - Complete it in this file
import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    player_choice = input ("Enter RPS choice (rock, paper, scissors):")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    if player_choice == "rock" and computer_choice == "scissors" or player_choice == "paper" and computer_choice == "rock" or player_choice == "scissors" and computer_choice == "paper":
        return "Winner is the player who chose: " + choices["player"] + " /" " Loser is the computer who chose: " + choices["computer"]
    elif player_choice == " scissors" and computer_choice =="rock" or player_choice == "rock" and computer_choice == "paper" or player_choice == "paper" and computer_choice == "scissors":
        return "Winner is the computer who chose: " + choices["computer"] + " /" " Loser is the player who chose: " + choices["player"]
    elif player_choice == computer_choice:
        return "It is a tie"
choices = play_game()
print(choices)