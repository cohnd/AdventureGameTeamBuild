# ------------------------------------------------------------------------
#
#  Function: hidden_trap
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player discovers a hidden trap that reduces health.
#
#  Author: Tyler Urben
#
# ------------------------------------------------------------------------

import random

def hidden_trap(health):
    # A list of traps. Each trap is a tuple: (name, low range, high range)
    traps = [
        ("tripwire", 3, 6),
        ("falling net", 5, 10),
        ("spike pit", 10, 15),
    ]

    # Pick one trap at random, then unpack its three parts into variables
    name, low, high = random.choice(traps)

    # Chance to spot the trap and avoid it
    if random.random() < 0.25:
        print(f"You spot the {name} just in time and step around it!")
        return health

    # Otherwise the trap hits
    damage = random.randint(low, high)
    health = health - damage

    print(f"You fell for a {name} trap!")
    print(f"You lose {damage} health.")

    # 0 HP floor: if health went below 0, set it to 1
    if health <= 0:
        health = 1

    return health