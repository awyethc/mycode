#!/usr/env python3

"""    Script Requirements:
    The user may take a Long Rest as long as they have at least 40 Camp Supplies
    The user may take up to 2 Short Rests before they run out
    Taking a Long Rest replenishes all short rests
    The user may Forage for Supplies to add to the Camp Supplies with some kind of d20 test
    Option to gracefully exit the script (without using CTRL+C)"""

import random

class Party:
    def __init__(self):
        self.camp_supplies = 0
        self.short_rests = 2
        self.long_rests = 0

    def take_long_rest(self):
        if self.camp_supplies >= 40:
            self.long_rests += 1
            self.short_rests = 2
            self.camp_supplies -= 40
            print("You take a Long Rest. All short rests are replenished.")
        else:
            print("You don't have enough Camp Supplies for a Long Rest.")

    def take_short_rest(self):
        if self.short_rests > 0:
            self.short_rests -= 1
            print("You take a Short Rest.")
        else:
            print("You've run out of Short Rests. Consider a Long Rest.")

    def forage_supplies(self):
        roll = random.randint(1, 20)
        if roll >= 10:
            supplies_found = random.randint(1, 10)
            self.camp_supplies += supplies_found
            print(f"You successfully foraged {supplies_found} Camp Supplies.")
        else:
            print("You couldn't find any additional Camp Supplies while foraging.")

    def show_status(self):
        print(f"Camp Supplies: {self.camp_supplies}")
        print(f"Short Rests left: {self.short_rests}")
        print(f"Long Rests taken: {self.long_rests}")

def main():
    party = Party()

    while True:
        print("\nChoose an action:")
        print("1. Take a Long Rest")
        print("2. Take a Short Rest")
        print("3. Forage for Supplies")
        print("4. Show Status")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            party.take_long_rest()
        elif choice == '2':
            party.take_short_rest()
        elif choice == '3':
            party.forage_supplies()
        elif choice == '4':
            party.show_status()
        elif choice == '5':
            print("Exiting the script.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
