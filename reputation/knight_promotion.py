# ------------------------------------------------------------------------
#  Function: knight_promotion
#
#  Inputs: title (string)
#  Returns: title (string)
#
#  Description: Player may be promoted to Knight depending on a 
#    random outcome.
#
#  Author: <Jared Johnson>
#
# ------------------------------------------------------------------------
import random
def knight_promotion(title):
    outcome = random.randint(1, 2)
    if outcome == 1:
        print("Congratulations! You have been promoted!")
        return "Lord Commander"
    else:
        print("You have not been promoted.")
        return title
    
if __name__ == "__main__":
    ret_val = knight_promotion("knight")
    print(ret_val)
