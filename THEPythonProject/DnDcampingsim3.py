#!/usr/env python3
import random

import random

# Define the possible environments
environments = ["forest", "island", "plains", "swamp", "mountain"]

# Define the number of supplies required for a long rest
long_rest_supplies = 40

# Define the bonus to the foraging roll for each environment
foraging_bonuses = {
    "forest": 8,
    "island": 5,
    "plains": 3,
    "swamp": 1,
    "mountain": -1,
}

# Start the script
while True:
    # Get the current amount of supplies
    supplies = int(input("Current amount of supplies: "))

    # Get the current environment
    environment = random.choice(environments)

    # Get the number of short rests remaining
    short_rests_remaining = int(input("Number of short rests remaining: "))

    # Prompt the user to make a choice
    print("Choose an option:")
    print("1. Take a long rest")
    print("2. Take a short rest")
    print("3. Forage for supplies")
    choice = int(input())

    # Do the corresponding action
    if choice == 1:
        # Take a long rest
        supplies -= long_rest_supplies
        short_rests_remaining = 2
        environment = random.choice(environments)
    elif choice == 2:
        # Take a short rest
        short_rests_remaining -= 1
    else:
        # Forage for supplies
        roll = random.randint(1, 20)
        bonus = foraging_bonuses[environment]
        if roll + bonus >= 10:
            # Found supplies
            supplies += 10
        else:
            # Didn't find supplies
            pass

    # Print the updated status
    print("Supplies:", supplies)
    print("Environment:", environment)
    print("Short rests remaining:", short_rests_remaining)

