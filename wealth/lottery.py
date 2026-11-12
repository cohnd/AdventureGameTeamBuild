# ------------------------------------------------------------------------
#
#  Function: lottery
#
#  Inputs: gold (integer)
#  Returns: gold (integer)
#
#  Description: Player gambles and wins a random amount of gold 
#    (could be zero).
#
#  Author: <Benjamin Botelho>
#
# ------------------------------------------------------------------------

import random

def lottery(gold):
    print("Lottery")
    
    winnings = random.randint(0, 100)
    print("Congratulations! You've won", winnings, "gold!")

    return gold + winnings

# Simple driver
gold = 10
new_gold = lottery(gold)

print("Your gold is now:", new_gold)