# ------------------------------------------------------------------------
#
#  Function: forest_attack
#
#  Inputs: health (integer)
#  Returns: health (integer)
#
#  Description: Player is attacked by wolves and loses a random amount 
#  of health.
#
#  Author: <Manuel Josue Parra Flores
#
# ------------------------------------------------------------------------

import random

def forest_attack(health):
    print("Forest Attack!")
    damage = random.randint(1, 5)
    return health-damage 
