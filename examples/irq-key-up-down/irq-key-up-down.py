"""
Prints which keys are pressed (0-4095), when any key is pressed or released.

The interrupt fires when any key is pressed or released.
"""

import mpr121
from machine import Pin

i2c = machine.I2C(3)
mpr = mpr121.MPR121(i2c)

# check all keys
def check(pin):
    print(mpr.touched())

d3 = Pin('D3', Pin.IN, Pin.PULL_UP)
d3.irq(check, Pin.IRQ_FALLING)
