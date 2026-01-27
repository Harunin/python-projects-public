"""
Program name: number_guessing_game.py
Programmer: Yuta Jellali
Date: 1-26-2026
Version: 1.0
Purpose: A fun number guessing game that the user has to figure out
"""

# Import module(s)
import random

# Display title
print("")
print("[Number Guessing Game]")
print("")

# Display user options
print("1. 1-25")
print("2. 1-50")
print("3. 1-99")
print("")

# User selects one of the shown user options
user_decision = 0
while user_decision < 0 or user_decision == 0 or user_decision > 3: #^ While loop for user decision
    user_decision = int(float(input("Please choose one of the options [1, 2, or 3]: ")))
    if user_decision < 0 or user_decision == 0 or user_decision < 1 or user_decision > 3: #^ Correction for invalid input
        print("Please try again")
        print("")
    else:
        print(f"You have chosen option {user_decision}") #^ Confirmation of user decision
        print("")
        print("")

# Game option 1
if user_decision == 1:
    users_guessing_number = 0
    guessing_number = random.randrange(1,26) #^ Generates random number (1-25) to guess
    while users_guessing_number != guessing_number: #^ Loop until correct number is guessed
        users_guessing_number = int(float(input("Enter a number to guess: ")))
        if users_guessing_number < guessing_number: #^ Provides guess hints
            print("HINT: The generated number is larger.")
            print("")
        elif users_guessing_number > guessing_number:
            print("HINT: The generated number is smaller.")
            print("")
    if users_guessing_number == guessing_number: #^ Tells user they guessed correct
        print("")
        print("YOU WIN!")
        print("")

# Game option 2
if user_decision == 2:
    users_guessing_number = 0
    guessing_number = random.randrange(1,51) #^ Generates random number (1-50) to guess
    while users_guessing_number != guessing_number: #^ Loop until correct number is guessed
        users_guessing_number = int(float(input("Enter a number to guess: ")))
        if users_guessing_number < guessing_number: #^ Provides guess hints
            print("HINT: The generated number is larger.")
            print("")
        elif users_guessing_number > guessing_number:
            print("HINT: The generated number is smaller.")
            print("") 
    if users_guessing_number == guessing_number: #^ Tells user they guessed correct
        print("")
        print("YOU WIN!")
        print("")

# Game option 3
if user_decision == 3:
    users_guessing_number = 0
    guessing_number = random.randrange(1,100) #^ Generates random number (1-99) to guess
    while users_guessing_number != guessing_number: #^ Loop until correct number is guessed
        users_guessing_number = int(float(input("Enter a number to guess: ")))
        if users_guessing_number < guessing_number: #^ Provides guess hints
            print("HINT: The generated number is larger.")
            print("")
        elif users_guessing_number > guessing_number:
            print("HINT: The generated number is smaller.")
            print("")
    if users_guessing_number == guessing_number: #^ Tells user they guessed correct
        print("")
        print("YOU WIN!")
        print("")