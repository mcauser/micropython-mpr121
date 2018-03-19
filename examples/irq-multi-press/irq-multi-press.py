"""
To solve this puzzle, you must press and hold keys 3, 7 and 11.
"""

import mpr121
from machine import Pin

i2c = machine.I2C(3)
mpr = mpr121.MPR121(i2c)

# the winning combination is 3, 7 and 11
combination = (1<<3) | (1<<7) | (1<<11)

# check all keys
def check(pin):
    t = mpr.touched()
    print(t)
    if t & combination == combination:
        print("You found the winning combination!")

d3 = Pin('D3', Pin.IN, Pin.PULL_UP)
d3.irq(check, Pin.IRQ_FALLING)
