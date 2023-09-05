#!/usr/bin/env python3


"""This script is meant to mimic the short and long rest mechanics from Baldur's Gate 3.
    
    Baldur's Gate 3 is copyright 2023 by Larian Studios, and Wizards of the Coast

    Coded with assistance from Google Bard

    Script Requirements:
    The user may take a Long Rest as long as they have at least 40 Camp Supplies
    The user may take up to 2 Short Rests before they run out
    Taking a Long Rest replenishes all short rests
    The user may Forage for Supplies to add to the Camp Supplies with some kind of d20 test
    Option to gracefully exit the script (without using CTRL+C)"""

import random

# Define the maximum and minimum values for CAMP_SUPPLIES.
CAMP_SUPPLIES_MAX = 160
CAMP_SUPPLIES_MIN = 0

# Define the number of short rests the user can take before they run out.
SHORT_RESTS_MAX = 2

# Define the d20 roll needed to successfully forage for supplies.
FORAGE_SUCCESS_ROLL = 15

# Create a variable to store the current number of camp supplies.
CAMP_SUPPLIES = 80

def main():
# Start a loop that will continue until the user exits the script.
    while True:
        global CAMP_SUPPLIES, SHORT_RESTS_MAX
  # Print the current number of camp supplies.
    print(f"You have {CAMP_SUPPLIES} camp supplies.")

  # Ask the user what they want to do.
    print("What do you want to do?")
    print("1. Take a long rest")
    print("2. Take a short rest")
    print("3. Forage for supplies")
    print("4. Exit")

  # Get the user's CHOICE.
    CHOICE = input()

  # If the user chooses to take a long rest, check if they have enough supplies.
    if CHOICE == "1":
      if CAMP_SUPPLIES >= 40:
        print("You take a long rest, using 40 supplies.")
        CAMP_SUPPLIES -= 40
      else:
          print("You don't have enough supplies for a long rest.")

  # If the user chooses to take a short rest, decrement the number of short rests remaining.
    elif CHOICE == "2":
        if SHORT_RESTS_MAX > 0:
        SHORT_RESTS_MAX -= 1
        print("You take a short rest.")
      else:
        print("You don't have any short rests remaining.")

    # If the user chooses to forage for supplies, roll a d20.
    elif CHOICE == "3":
      roll = random.randint(1, 20)

    # If the roll is successful, add 10 to the number of camp supplies.
      if roll >= FORAGE_SUCCESS_ROLL:
        CAMP_SUPPLIES += 10
        print("You successfully forage for supplies and find 10 more.")
      else:
        print("You fail to forage for supplies.")

    #If the user chooses to exit, break out of the loop.
    elif CHOICE == "4":
      exit()

    # Otherwise, print an error message.
    else:
      print("Invalid input, please use options 1 through 4")

if __name__ == "__main__":
    main()
