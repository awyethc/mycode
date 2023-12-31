#!/usr/env python3

"""    Script Requirements:
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

import random
import time

class Party:
    """Create a Party class that will hold attributes"""
    def __init__(self):
        self.camp_supplies = 80 #Start with 80 camp supplies.
        self.short_rests = 2 #Short rest counter

    def take_long_rest(self):
        """Take a short rest if the party has more than 40 camp supplies."""
        if self.camp_supplies >= 40:
            self.short_rests = 2 # Reset the short rest counter
            self.camp_supplies -= 40 # Consume 40 Camp Supplies
            print("\nYou consume 40 Camp Supplies and take a Long Rest.\n")
            print("\nAll short rests have been replenished.")
        else:
            print("\nYou don't have enough Camp Supplies for a Long Rest.")

    def take_short_rest(self):
        """Take a short rest if the party has any left"""
        if self.short_rests > 0:
            self.short_rests -= 1
            print("\nYou take a Short Rest.")
            print(f"You have {self.short_rests} Short Rests remaining.")
        else:
            print("\nYou've run out of Short Rests. Consider a Long Rest.")

    def forage_supplies(self):
        """Try to forage for supplies"""
        roll = random.randint(1, 20)
        if roll >= 10:
            supplies_found = random.randint(1, 10)
            self.camp_supplies += supplies_found
            print(f"\nYou successfully foraged {supplies_found} Camp Supplies.")
        else:
            print("\nYou couldn't find any additional Camp Supplies while foraging.")

    def show_status(self):
        """Let the user check the party resources"""
        print(f"\nCamp Supplies: {self.camp_supplies}")
        print(f"Short Rests remaining: {self.short_rests}")

def main():
    """Main function, which calls the Party class"""
    party = Party()

    while True:
        print("\nChoose an action:")
        print("1. Take a Long Rest")
        print("2. Take a Short Rest")
        print("3. Forage for Supplies")
        print("4. Show Status")
        print("5. Exit")

        choice = input("\nEnter your choice (1/2/3/4/5): ")
        time.sleep(0.5)

        if choice == '1':
            party.take_long_rest()
        elif choice == '2':
            party.take_short_rest()
        elif choice == '3':
            party.forage_supplies()
        elif choice == '4':
            party.show_status()
            time.sleep(1)
        elif choice == '5':
            print("\nThank you for playing, this sim will exit in 3 seconds.\n")
            time.sleep(3)
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
