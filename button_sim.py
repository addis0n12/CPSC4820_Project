# Interactivity Example PR1d
# Addison Hough, Lucas Grijak

from pgzero.builtins import Actor, keyboard, keys

import random
import time
import sys
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

# variable to represent current lot button is registered to
# will default as C1
current_lot = "C1"

# Actors for the button and the light
lit_button = Actor("lit_button.png")
unlit_button = Actor("unlit_button.png")

# currently must be rerun for new button state, will be changed in future
def draw():
    unlit_button.draw()
    if commuter_lots.get(current_lot) == 0:
        lit_button.draw()

# function used to re-randomize lot status after a random amount of time
def randomize_state():
    commuter_lots.update({
        "C1": random.choice([1, 0]),
        "C2": random.choice([1, 0]),
        "C3": random.choice([1, 0]),
        "C11": random.choice([1, 0])
    })
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

# funcition used to set current lot button is tracking to user selection
def set_lot(lot_name):
    global current_lot
    current_lot = lot_name

def on_key_down(key):
    if keyboard.k_1:
        print("Lot C1 Selected")
        set_lot("C1")
    elif keyboard.k_2:
        print("Lot C2 Selected")
        set_lot("C2")
    elif keyboard.k_3:
        print("Lot C3 Selected")
        set_lot("C3")
    elif keyboard.k_4:
        print("Lot C11 Selected")
        set_lot("C11")
    elif keyboard.r:
        print("Rerolling lot states")
        randomize_state()
    else:
        print("Invalid Selection, please selected 1 through 4")
