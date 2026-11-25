# ------------------------------------------------------------------------
#  Function: healing_herbs
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player finds healing herbs that restore health
#
#  Author: Abdi Sherif
# ------------------------------------------------------------------------
# This brings in Python's random module for picking random herbs 
import random

# This defines the function
def healing_herbs(health):
    # A list of herb names the player might find
    herbs = ["tarragon", "bay leaf", "marjoram"]
    # Pick one herb from the list 
    herb = random.choice(herbs)
    # Pick a random whole number from 3 to 8 
    heal = random.randint(3, 8)
    # Tells the player what they found
    print(f"You found {herb} in a magic grove.")
    # Tells the player how much health they have 
    print(f"You eat a small portion of {heal} health.")
    # Adds healing amount to the player's health
    health = health + heal
    # Sends the new health value back 
    return health
