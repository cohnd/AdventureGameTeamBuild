# ------------------------------------------------------------------------
#
#  Function: find_treasure
#
#  Inputs: gold (integer)
#  Returns: gold (integer)
#
#  Description: Player finds treasure and gains a random amount of gold.
#
#  Author: Steven Peltier
#
# ------------------------------------------------------------------------

import random

def find_treasure(gold):
    print("Find Treasure")
    treasure_amount = random.randint(200, 2000)
    print(f"You found {treasure_amount} gold!")
    return gold + treasure_amount