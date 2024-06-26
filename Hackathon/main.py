import Utilities
from random import randint

# Scanner
scan = "change"
#
#
#
#
#
name = ""  # Given
score = 20  # Given
prize = ""  # Given
people = {name: [score, prize]}
# Score Change

Utilities.win(people, name, scan)

# Reward
Pressed = "Yes"
if Pressed == "Yes":  # if button pressed
    Utilities.reward(people, name)
