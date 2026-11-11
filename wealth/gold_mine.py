# ------------------------------------------------------------------------
# 
#  Function: gold_mine
#  
#  Inputs: gold (integer)
#  Returns: gold (integer)
 # --- Game loop ---
    game_active = True
    while game_active:
        # --- Display stats ---
        print()
        status_report(health, gold, title)
#  from wealth.gold_mine import gold_mine
      print()
        print("Choose what to do:")
        print("1 - Advance Reputation")
        print("2 - Face Encounter")
        print("3 - Increase Wealth")
        print("4 - Quit")
#  Description: Player discovers a gold mine and gains a substantial
#    amount of gold.
#  gold_functions = [
        find_treasure, bandit_ambush, merchant_sale, find_gem,
        duel_knight, gold_mine, cursed_coin, treasure_map, lottery
    ]
 # --- Wealth ---
        elif choice == "3":
            func = random.choice(gold_functions)
            gold = func(gold)

        # --- Quit ---
        else:
            print("Thanks for playing!")
            game_active = False
#  
#  Author: <I.J. Acuna>
#
# ------------------------------------------------------------------------

import random

def gold_mine(gold):
    print("Gold Mine")
    return gold+5
