# ------------------------------------------------------------------------
#
#  Function: validate_choice
#
#  Inputs: prompt (string), choices (list of valid strings)
#  Returns: valid user choice (string)
#
#  Description: Keeps asking the user for input until they enter one of 
#    the allowed choices. Ensures the menu never crashes.
#
#  Author: Austin Morris
#
# ------------------------------------------------------------------------

def validate_choice(prompt, choices):
    choice = input(prompt).strip()

    while choice not in choices:
        print("That's not possible, please try again")
        choice = input(prompt).strip()

    return choice