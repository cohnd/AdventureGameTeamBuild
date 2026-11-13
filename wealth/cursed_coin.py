import random


def cursed_coin(gold):
    outcomes = [-5, -5, -5, -5, -15, -15, 10, 10]
    gold_change = random.choice(outcomes)
    print("You have encountered a gold coin oooooo SPOOKY!!")
    if gold_change < 0:
        print("The gold coin glows red")
        print(f"You have lost {abs(gold_change)} coins boohoo ")
    elif gold_change > 0:
        print("The gold coin glows green niceeee!")
        print(f"You have won {gold_change} coins congrats.")
    print(f"You have {gold + gold_change} coins left in your bag.")
    return gold + gold_change

gold = 100
gold = cursed_coin(gold)