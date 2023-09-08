#!/usr/env python3

"""    Script Requirements:
    The user may take a Long Rest as long as they have at least 40 Camp Supplies (DONE)
    The user may take up to 2 Short Rests before they run out (DONE)
    Taking a Long Rest replenishes all short rests (DONE)
    The user may Forage for Supplies to add to the Camp Supplies with some kind of d20 test (DONE)
    Option to gracefully exit the script (without using CTRL+C) (DONE)
    
    Nice to haves:
    Chance to change to a different ENVIRONMENT (aka biome, at least 5), after a LONG_REST (DONE)
    Environments can affect Long Rests, Short Rests, and Foraging (DONE)
    Text presented to the user clearly dilineated and easy to read (DONE-ish)
    Do not present options that are unavailable, such as LONG_REST when CAMP_SUPPLIES < 40 (SCRAPPED, encourage statusget)
    Feedback and return to options when user input is an unexpected arg (SCRAPPED, encourage statusget)
    Ask user how many supplies they are starting with (max 80) (NOT DONE)
    User can replenish 1 SHORT_REST if they try to LONG_REST with <40 CAMP_SUP, but >20+ CAMP_SUP (NOT DONE)
    
    Add random happenings for Short Rests, Long Rests, and Foraging. Such as
    Goblins raided your camp while you were away! You lost X Camp Supplies!
    -or-
    You encountered a trading caravan and bartered for extra supplies! (+10)
      etc etc.

    Add module for diverse supplies, dependant on environment.
    Give said supplies their own values, (e.g. Sausage is 5, cheese is 4, etc)

    Player/Party Member determined modifiers. Would require a party roster section.

    Move the environment section to an external library and learn to use the
    from <module> import <class/variable/method> code better.
    
    Clean up grammar"""

# Import the modules needed for script functionality.
import random # Could be subbed out for dice.py later?
import time # Chronomancy is the strongest magic

class Party:
    """Create a Party class that will hold the relevant attributes"""
    def __init__(self):
        self.camp_supplies = 80  # Start with 80 camp supplies.
        self.short_rests = 2   # Short rest counter
        self.weather = ""
        self.biome = ""
        self.change_environment()  # Initialize the environment, storing them in self.weather and self.biome

    def take_long_rest(self):
        """Take a short rest if the party has more than 40 camp supplies."""
        if self.camp_supplies >= 40:
            self.short_rests = 2   # Reset the short rest counter
            self.camp_supplies -= 40  # Consume 40 Camp Supplies
            print("\nYou consume 40 Camp Supplies and take a Long Rest.")
            print("\nAll short rests have been replenished.")
            print("\nThe Party packs up and moves on to the next area...") # hint hint, check status
            self.change_environment()  # Report environment after a long rest
        else:
            print("\nYou don't have enough Camp Supplies for a Long Rest.")

    def take_short_rest(self):
        """Take a short rest if the party has any left"""
        if self.short_rests > 0:
            self.short_rests -= 1
            print("\nYou take a Short Rest.")
            print(f"You have {self.short_rests} Short Rests remaining.")
            self.change_weather()  # Change weather after a short rest
        else:
            print("\nYou've run out of Short Rests. Consider a Long Rest.")

    def report_environment(self):
        """Report the current environment (weather and biome)."""
        print(f"\nCurrent Biome: {self.biome}")
        print(f"Current Weather: {self.weather}")
        print(f"Camp Supplies: {self.camp_supplies}")
        print(f"Short Rests remaining: {self.short_rests}")

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
            supplies_found = random.randint(1, 10) # Determine amount of supplies found
            print(f"\nYou successfully foraged {supplies_found} Camp Supplies.")
            self.camp_supplies += supplies_found  # Add found supplies to camp_supplies
        else: 
            print("\nYou couldn't find any additional Camp Supplies while foraging.")
            return 0 # If the roll doesn't clear the DC, signal to the calling code that no supplies are added

    def change_weather(self):
        """Change the weather after a short rest."""
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
        new_weather = random.choice(weather_options)
        if new_weather != self.weather:
            print(f"\nThe weather has become {new_weather}.")
            self.weather = new_weather
        else:
            print(f"\nThe weather remains {self.weather}.")

    def change_environment(self):
        """Change both the weather and biome (used during initialization and long rest)."""
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

def main():
    """Main function, which calls the Party class"""
    party = Party()

    # Initial message to the user on first start up
    print("\nWelcome to the Rest Mechanics Simulator!\n")
    print(f"Your party is located in a {party.biome} biome, and the weather is currently {party.weather}.\n")
    print(f"You have {party.camp_supplies} Camp Supplies remaining.")
    time.sleep(1)

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
            party.take_long_rest() # Call the take_long_rest method, changing the environment (biome + weather)
        elif choice == '2':
            party.take_short_rest() # Call the take_short_rest method, possibly changing the weather
        elif choice == '3':
            party.calculate_forage_amount()  # Call the calculate_forage_amount method, possibly adding supplies
        elif choice == '4':
            party.report_environment() # Call the report_environment method for status info
        elif choice == '5':
            print("\nThank you for traveling with us!\n") # Begin to gracefully exit the simulator
            print("The Rest Mechanics simulator will exit in 3 seconds.\n")
            print("Have a wonderful day!")
            time.sleep(3)
            break
        else:
            print("\nInvalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()