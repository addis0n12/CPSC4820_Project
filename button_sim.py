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

# Just testing the pygame zero install, was having some issues getting it working
lit_button = Actor("lit_button.png")

def draw():
    lit_button.draw()

