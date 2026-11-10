# ------------------------------------------------------------------------
#
#  Function: magical_training
#
#
#  Description: Player undergoes magical training and gains a more
#    prestigious title, where "Wise " is added to the front of it.
#
#  Author: Kaylie Blood
#
# ------------------------------------------------------------------------

import random

def magical_training(title):
    teachers = [
        "a grumpy old archmage",
        "a talking owl",
        "a retired dragon",
        "a very patient gnome",
    ]
    teacher = random.choice(teachers)
    print(f"You train with {teacher} and master the arcane arts.")
    print("Your mind expands. You have earned a new title!")
    return "Wise " + title
