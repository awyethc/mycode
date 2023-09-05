#!/usr/env python3
import random

def get_user_choice():
  """Gets the user's choice of what to do."""
  print("What would you like to do?")
  print("1. Take a long rest")
  print("2. Take a short rest")
  print("3. Forage for supplies")
  choice = input("Enter your choice (1-3): ")
  return choice

def take_long_rest(supplies, short_rests):
  """Takes a long rest, consuming 40 supplies and refreshing the number of short rests."""
  supplies -= 40
  short_rests = 2
  print("You take a long rest. You have {} supplies remaining and {} short rests remaining.".format(supplies, short_rests))

def take_short_rest(short_rests):
  """Takes a short rest, consuming no supplies."""
  if short_rests > 0:
    short_rests -= 1
    print("You take a short rest. You have {} short rests remaining.".format(short_rests))
  else:
    print("You cannot take a short rest. You have already taken the maximum number of short rests for the day.")

def forage_for_supplies(supplies, environment):
  """Forages for supplies, rolling a d20 and adding a bonus based on the environment."""
  bonus = {
    "forest": 8,
    "island": 5,
    "plains": 3,
    "swamp": 1,
    "mountain": -1
  }
  roll = random.randint(1, 20) + bonus[environment]
  if roll >= 10:
    supplies += 10
    print("You successfully forage for supplies. You now have {} supplies.".format(supplies))
  else:
    print("You did not find any supplies. You still have {} supplies.".format(supplies))

def main():
  """The main function of the script."""
  supplies = 100
  short_rests = 2
  environment = "forest"

  while True:
    print("You have {} supplies, {} short rests, and are in the {} environment.".format(supplies, short_rests, environment))
    choice = get_user_choice()

    if choice == "1":
      take_long_rest(supplies, short_rests)
    elif choice == "2":
      take_short_rest(short_rests)
    elif choice == "3":
      forage_for_supplies(supplies, environment)
    else:
      print("Invalid choice.")

if __name__ == "__main__":
  main()
