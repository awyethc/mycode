#!/usr/env python3

"""This script is meant to mimic the short and long rest mechanics from Baldur's Gate 3.
    
    Baldur's Gate 3 is copyright 2023 by Larian Studios, and Wizards of the Coast

    Coded with assistance from Google Bard

    Script Requirements:
    The user may take a Long Rest as long as they have at least 40 Camp Supplies
    The user may take up to 2 Short Rests before they run out
    Taking a Long Rest replenishes all short rests
    The user may Forage for Supplies to add to the Camp Supplies with some kind of d20 test
    Option to gracefully exit the script (without using CTRL+C)
    
    Nice to haves:
    Chance to change to a different ENVIRONMENT (aka biome, at least 5), after a LONG_REST
    Environments can affect Long Rests, Short Rests, and Foraging
    Text presented to the user clearly dilineated and easy to read
    Do not present options that are unavailable, such as LONG_REST when CAMP_SUPPLIES < 40
    Feedback and return to options when user input is an unexpected arg
    Ask user how many supplies they are starting with (max 80)
    User can replenish 1 SHORT_REST if they try to LONG_REST with <40 CAMP_SUP, but >20+ CAMP_SUP"""

#Import modules needed
import random

# Initialize the variables

SUPPLIES = 100
SHORT_RESTS_REMAINING = 2
ENVIRONMENT = "forest"

# Prompt the user for their choice
while True:
    print("Current supplies:", SUPPLIES)
    print("Current biome:", ENVIRONMENT)
    print("Short rests remaining:", SHORT_RESTS_REMAINING)
    print("Choose an option:")
    print("1. Take a long rest")
    print("2. Take a short rest")
    print("3. Forage for supplies")

    choice = input("Enter your choice: ")

    # Handle the user's choice
    if choice == "1":
        # Take a long rest
        SUPPLIES -= 40
        SHORT_RESTS_REMAINING = 2
        ENVIRONMENT = random.choice(["forest", "plains", "mountains", "swamp", "island"])
    elif choice == "2":
        # Take a short rest
        if SHORT_RESTS_REMAINING > 0:
            SHORT_RESTS_REMAINING -= 1
        else:
            print("You have no short rests remaining.")
    elif choice == "3":
        # Forage for supplies
        roll = random.randint(1, 20)
        if ENVIRONMENT  == "forest":
            roll += 8
        elif ENVIRONMENT    == "island":
            roll += 5
        elif ENVIRONMENT    == "plains":
            roll += 3
        elif ENVIRONMENT    == "swamp":
            roll += 1
        elif ENVIRONMENT    == "mountains":
            roll -= 1

        if roll >= 10:
            SUPPLIES += 10
            print("You found 10 camping supplies.")
        else:
            print("You didn't find any camping supplies.")
    else:
        print("Invalid choice.")