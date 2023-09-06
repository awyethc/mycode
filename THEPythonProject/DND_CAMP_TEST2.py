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
        self.camp_supplies = 80  # Start with 80 camp supplies
        self.short_rests = 2 # Start with 2 Short Rests Available
        self.weather = "" # Starting as an empty string to be filled later
        self.biome = "" # Starting as an empty string to be filled later

    def take_long_rest(self):
        """Take a long rest if the party has more than 40 camp supplies."""
        if self.camp_supplies >= 40:
            self.short_rests = 2  # Reset short rest counter
            self.camp_supplies -= 40  # Consume 40 camp supplies
            self.report_environment()  # Generate new environment after the long rest
            print("\nYou consume 40 Camp Supplies and take a Long Rest.")
            print("\nAll short rests have been replenished.")
            print("\nThe Party packs up and moves on to the next area...") # hint hint, check status
        else:
            print("\nYou don't have enough Camp Supplies for a Long Rest.")
            print("\nYou will need to forage for more.")

    def take_short_rest(self):
        """Take a short rest if the party has any left
            and report any changes in the weather"""
        old_weather = self.weather  # Store the current weather before the short rest
        if self.short_rests > 0:
            self.short_rests -= 1
            self.report_environment()  # Report the environment after a short rest
            new_weather = self.weather  # Get the new weather after the short rest

            time.sleep(0.5)
            if new_weather != old_weather:
                print("\nYou take a Short Rest.")
                print(f"The weather has become {new_weather}.")
            else:
                print("\nYou take a Short Rest.")
                print(f"The weather remains {new_weather}.")

            time.sleep(1)
            print(f"\nYou have {self.short_rests} Short Rests remaining.")
        else:
            print("\nYou've run out of Short Rests. Consider a Long Rest.")

    def forage_supplies(self):
        """Try to forage for supplies in the current environment and weather conditions"""
        roll = random.randint(1, 20)
        if roll >= 10:
            supplies_found = self.calculate_forage_amount()
            self.camp_supplies += supplies_found
            print(f"\nYou successfully foraged {supplies_found} Camp Supplies.")
        else:
            print("\nYou couldn't find any additional Camp Supplies while foraging.")

    def calculate_forage_amount(self):
        """Calculate the amount of supplies to forage based on the environment."""
        roll = random.randint(1, 20)
        environment_modifiers = {
            "Sunny": random.randint(1, 10),  # Random modifier between 1 and 10
            "Windy": random.randint(1, 4),   # Random modifier between 1 and 4
            "Misty": random.randint(1, 6),   # Random modifier between 1 and 6
            "Blizzard": -random.randint(1, 10),  # Random negative modifier between 1 and 10
            "Dusty": -random.randint(1, 6),  # Random negative modifier between 1 and 6
            "Light Rain": random.randint(1, 6),  # Random modifier between 1 and 6
            "Heavy Rain": -random.randint(1, 4),  # Random negative modifier between 1 and 4
            "Snowy": -random.randint(1, 6),  # Random negative modifier between 1 and 6
            "Overcast": random.randint(1, 8),  # Random modifier between 1 and 8
            "Partly Cloudy": random.randint(1, 6),  # Random modifier between 1 and 6
            "Stormy": -random.randint(1, 8),  # Random negative modifier between 1 and 8
            "Foggy": -random.randint(1, 6)  # Random negative modifier between 1 and 6
        }
        biome_modifiers = {
            "Forest": 2,
            "Plains": 1,
            "Island": 0,
            "Mountain": -1,
            "Swamp": -2,
            "Desert": -3,
            "Tundra": -3,
            "Cave": -4,
            "Coastal": 1,
            "Jungle": 1
        }
    weather_modifier = environment_modifiers.get(self.weather, 0)

    biome_modifier = biome_modifiers.get(self.biome, 0)
    total_modifier = weather_modifier + biome_modifier

    if roll + total_modifier >= 10:
        supplies_found = random.randint(1, 10)
        print(f"\nYou successfully foraged {supplies_found} Camp Supplies.")
        return supplies_found
    else:
        print(f"\nYou couldn't find any additional Camp Supplies while foraging.")
        return 0


    def report_environment(self):
        """Generate the current environment (weather and biome)."""
        weather_options = [
        "Sunny",
        "Windy",
        "Misty",
        "Blizzard",
        "Dusty",
        "Light Rain",
        "Heavy Rain",
        "Snowy",
        "Overcast",
        "Partly Cloudy",
        "Stormy",
        "Foggy"
    ]
        biome_options = [
        "Forest",
        "Plains",
        "Island",
        "Mountain",
        "Swamp",
        "Desert",
        "Tundra",
        "Cave",
        "Coastal",
        "Jungle"  
    ]
        self.weather = random.choice(weather_options)
        self.biome = random.choice(biome_options)

    def show_status(self):
        """Let the user check the party resources and environment."""
        print(f"\nCamp Supplies: {self.camp_supplies}")
        print(f"Short Rests remaining: {self.short_rests}")
        print(f"Weather: {self.weather}")
        print(f"Biome: {self.biome}")

def main():
    """Main function, which calls the Party class"""
    party = Party()

    party.report_environment() # The first time the report environment function is called

    # Initial message to the user on first start up
    print("\nWelcome to the Rest Mechanics Simulator!\n")
    print(f"Your party is located in a {party.biome} biome, and the weather is currently {party.weather}.\n")
    print(f"You have {party.camp_supplies} Camp Supplies remaining.")
    time.sleep(1)

    while True:
        time.sleep(1)
        print("\nChoose your next course of action:")
        time.sleep(1)
        print("1. Take a Long Rest (costs 40 Camp Supplies)")
        print("2. Take a Short Rest")
        print("3. Forage for Supplies")
        print("4. Show Status")
        print("5. Exit")

        choice = input("\nEnter your choice (1/2/3/4/5): ")
        time.sleep(0.25)

        if choice == '1':
            party.take_long_rest()
        elif choice == '2':
            party.take_short_rest()
        elif choice == '3':
            party.forage_supplies()
        elif choice == '4':
            party.show_status()
            time.sleep(2)
        elif choice == '5':
            print("\nThank you for traveling with us!\n")
            print("The Rest Mechanics simulator will exit in 3 seconds.\n")
            print("Have a wonderful day!")
            time.sleep(3)
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
