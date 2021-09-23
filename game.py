# this is the "game.py" file...

import random

import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")

print("Welcome", x, "ROCK, PAPER, SCISSORS, SHOOT!")

# PROMPT USER FOR INPUT

#x = input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("Choose 'rock' or 'paper' or 'scissors': ")
print("User chose:")
print(user_choice)

# COMPUTER CHOICE (AT RANDOM)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")
print (computer_choice)

if (user_choice == "rock") and (computer_choice == "rock"):
    print("TIE.")
elif (user_choice == "scissors") and (computer_choice == "scissors"):
    print("TIE.")
elif (user_choice == "paper") and (computer_choice == "paper"):
    print("TIE.")
elif (user_choice == "rock") and (computer_choice == "paper"):
    print("SORRY, YOU LOST. :(")
elif (user_choice == "rock") and (computer_choice == "scissors"):
    print("CONGRATULATIONS, YOU WON! :)")
elif (user_choice == "paper") and (computer_choice == "scissors"):
    print("SORRY, YOU LOST :(")
elif (user_choice == "paper") and (computer_choice == "rock"):
    print("CONGRATULATIONS, YOU WON! :)")
elif (user_choice == "scissors") and (computer_choice == "rock"):
    print("SORRY, YOU LOST. :(")
elif (user_choice == "scissors") and (computer_choice == "paper"):
    print("CONGRATULATIONS, YOU WON! :)")

#adapted from Ryan Knapick on Slack (https://app.slack.com/client/TERLN9HL6/C02BNKRKZV5)
elif(user_choice != 'rock' or 'paper' or 'scissors'):
    print ("Something doesn't look right. Try again, and remember to use lowercase letters only.")

print("THANKS FOR PLAYING. PLEASE PLAY AGAIN!")