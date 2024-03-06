# Interactivity Example PR1c
# Addison Hough

import random
import moveWinHome

#https://pygame-zero.readthedocs.io/en/stable/

WIDTH  = 800
HEIGHT = 800

# Should probably have more commuter lots, but for now this is all
commuter_lots = {
    "C1": random.choice([1, 0]),
    "C2": random.choice([1, 0]),
    "C3": random.choice([1, 0]),
    "C11": random.choice([1, 0])
}

# Actors for the button and the light
lit_button = Actor("lit_button.png")
unlit_button = Actor("unlit_button.png")

# currently only selects the button state once per time that it is run, will be changed later
def draw():
    unlit_button.draw()
    if commuter_lots.get("C1") == 0:
        lit_button.draw()

