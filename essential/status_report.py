# ------------------------------------------------------------------
#
# Function: status_report
#
# Inputs: health (int), gold (int), title (string)
# Returns: none
#
# Description: Displays the player's current health, gold, and title
# in a format that's easy to read quickly.
#
# Author: Jenasi Santana
#
# ------------------------------------------------------------------

def status_report(health, gold, title):

    print("Status Report")
    print("================================")
    print("         PLAYER STATUS")
    print("================================")
    print(f"Title : {title}")
    print(f"Health: {health}")
    print(f"Gold  : {gold}")
    print("================================")