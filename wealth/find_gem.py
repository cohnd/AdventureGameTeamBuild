# ------------------------------------------------------------------------
#
#  Function: find_gem
#
#  Inputs: gold (integer)
#  Returns: gold (integer)
#
#  Description: Player finds a gem worth a random amount of gold.
#
#  Author: <Quentin Jackson>
#
# ------------------------------------------------------------------------

import random

def find_gem(gold):
    
    appraisal = random.randint(5,100)
    print(f"You found a Gem that was worth {appraisal} gold!")
    return gold+appraisal
