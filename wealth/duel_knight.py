# ------------------------------------------------------------------------
#
#  Function: duel_knight
#
#  Inputs: gold (integer)
#  Returns: gold (integer)
#
#  Description: Player gains random amount of gold from winning a duel.
#
#  Author: <Sean Phillips>
#
# ------------------------------------------------------------------------

import random

def duel_knight(gold):
    print("You came across another knight, time to duel!!")

    winnings = random.randint(1, 100)
    print("You won the duel and earned", winnings, "gold!")

    return gold + winnings

gold = 1
gold = duel_knight(gold)

print("Your gold is now:", gold)
