# ------------------------------------------------------------------------
#
#  Function: treasure_map
#
#  Inputs: gold (integer)
#  Returns: gold (integer)
#
#  Description: Player finds a treasure map, follows it, and gains gold.
#    The map may lead to a big haul, a small stash, or turn out to be a
#    fake, so the payoff is random.
#
#
#  Author: Daniel Cohn
#
# ------------------------------------------------------------------------

import random

def treasure_map(gold):
    print("You found a tattered treasure map!")
    print("You follow the trail to a big red X...")

    outcome = random.randint(1, 10)

    if outcome <= 2:
        # 20% - the map was a fake
        print("It was a fake map. You dug all day and found nothing.")
        found = 0
    elif outcome <= 7:
        # 50% - a modest stash
        found = random.randint(10, 30)
        print(f"You dug up a small chest holding {found} gold!")
    else:
        # 30% - the jackpot
        found = random.randint(40, 80)
        print(f"Jackpot! You unearthed a buried hoard worth {found} gold!")
    return gold + found