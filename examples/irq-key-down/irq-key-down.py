"""
Prints "Key n pressed" on key down.
Prints duplicates when multiple key are pressed.

The interrupt fires when any key is pressed or released.
Without storing previous state, on the n+1th key down all keys are treated
as just pressed.
"""

import mpr121
from machine import Pin

i2c = machine.I2C(3)
mpr = mpr121.MPR121(i2c)

# check keys one by one
def handler(p):
    for i in range(12):
        if mpr.is_touched(i):
            print('Key {} pressed'.format(i))

d3 = Pin('D3', Pin.IN, Pin.PULL_UP)
d3.irq(lambda p:handler(p), Pin.IRQ_FALLING)
