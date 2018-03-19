"""
Prints "Key n pressed" on key down.
Prints duplicates when multiple key are pressed.

Using a loop is not very precise as the key needs to be held at the start
of each iteration and if the key is held during the next iteration, will
introduce duplicate presses.

Without storing previous state, on the n+1th key down all keys are treated
as just pressed.
"""

import mpr121
from machine import Pin

i2c = machine.I2C(3)
mpr = mpr121.MPR121(i2c)

import time

# check keys one by one
while True:
    for i in range(12):
        if mpr.is_touched(i):
            print('Key {} pressed'.format(i))
    time.sleep_ms(100)
