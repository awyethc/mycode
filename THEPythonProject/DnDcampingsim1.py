#!/usr/env python3
import random

# Initialize the variables
supplies = 100
short_rests_remaining = 2
environment = "forest"

# Prompt the user for their choice
while True:
    print("Current supplies:", supplies)
    print("Current environment:", environment)
    print("Short rests remaining:", short_rests_remaining)
    print("Choose an option:")
    print("1. Take a long rest")
    print("2. Take a short rest")
    print("3. Forage for supplies")

    choice = input("Enter your choice: ")

    # Handle the user's choice
    if choice == "1":
        # Take a long rest
        supplies -= 40
        short_rests_remaining = 2
        environment = random.choice(["forest", "plains", "mountains", "swamp", "island"])
    elif choice == "2":
        # Take a short rest
        if short_rests_remaining > 0:
            short_rests_remaining -= 1
        else:
            print("You have no short rests remaining.")
    elif choice == "3":
        # Forage for supplies
        roll = random.randint(1, 20)
        if environment == "forest":
            roll += 8
        elif environment == "island":
            roll += 5
        elif environment == "plains":
            roll += 3
        elif environment == "swamp":
            roll += 1
        elif environment == "mountains":
            roll -= 1

        if roll >= 10:
            supplies += 10
            print("You found 10 camping supplies.")
        else:
            print("You didn't find any camping supplies.")
    else:
        print("Invalid choice.")
