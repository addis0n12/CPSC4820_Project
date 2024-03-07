# Interactivity Example PR1c
# Addison Hough, Lucas Grijak

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

# currently must be rerun for new button state, will be changed in future
def draw():
    if (commuter_lots.get("C1") == 1):
        print("C1: Full")
    else:
        print("C1: Not Full")

    if (commuter_lots.get("C2") == 1):
        print("C2: Full")
    else:
        print("C2: Not Full")

    if (commuter_lots.get("C3") == 1):
        print("C3: Full")
    else:
        print("C3: Not Full")

    if (commuter_lots.get("C11") == 1):
        print("C11: Full")
    else:
        print("C11: Not Full")

    unlit_button.draw()
    if commuter_lots.get("C1") == 0:
        lit_button.draw()
