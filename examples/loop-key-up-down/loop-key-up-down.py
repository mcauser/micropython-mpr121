"""
Prints which keys are pressed (0-4095), when any key is pressed or released.

Using a loop is not very precise as the key needs to be held at the start
of each iteration and if the key is held during the next iteration, will
introduce duplicate presses.
"""

import mpr121
from machine import Pin, I2C

i2c = I2C(3) # stm32
#i2c = I2C(scl=Pin(5), sda=Pin(4)) # esp8266
#i2c = I2C(scl=Pin(22), sda=Pin(21)) # esp32

mpr = mpr121.MPR121(i2c)

import time

# check all keys
while True:
    print(mpr.touched())
    time.sleep_ms(100)
