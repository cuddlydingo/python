import sys
from ex36_modules import *

print("Welcome to the Quest-iest Quest that ever Quested.\n\
      It's dangerous out there, so first, some questions....")

player_name = input("What... is your name? ")
player_quest = input("What... is your quest? ")
airspeed_velocity_of_coconut_laden_swallow = input("What... \
    is the airspeed velocity of a coconut-laden swallow? ")

if "african or european" in airspeed_velocity_of_coconut_laden_swallow:
    explode_bridgekeeper()
    exit(0)
else:
    print(f"Ahhhh, {player_name}... You may proceed.")
    begin_journey()
