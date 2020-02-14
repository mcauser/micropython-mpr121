"""
Prints "Key n pressed" on key down.
Prints "Key n released" on key up.

The interrupt fires when any key is pressed or released.
Detects changes from previous state and supports multiple concurrent key downs.
"""

import mpr121
from machine import Pin, I2C

i2c = I2C(3) # stm32
#i2c = I2C(scl=Pin(5), sda=Pin(4)) # esp8266
#i2c = I2C(scl=Pin(22), sda=Pin(21)) # esp32

mpr = mpr121.MPR121(i2c)

last = 0

def check(pin):
    global last
    touched = mpr.touched()
    diff = last ^ touched
    for i in range(12):
        if diff & (1 << i):
            if touched & (1<<i):
                print('Key {} pressed'.format(i))
            else:
                print('Key {} released'.format(i))
    last = touched

d3 = Pin('D3', Pin.IN, Pin.PULL_UP)
d3.irq(check, Pin.IRQ_FALLING)
