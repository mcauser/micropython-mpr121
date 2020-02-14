"""
Prints the filtered data and baseline values for a single key
"""

import mpr121
from machine import Pin, I2C

i2c = I2C(3) # stm32
#i2c = I2C(scl=Pin(5), sda=Pin(4)) # esp8266
#i2c = I2C(scl=Pin(22), sda=Pin(21)) # esp32

mpr = mpr121.MPR121(i2c)

# get the filtered data for key 0
mpr.filtered_data(0)
# not pressed value = 350
# pressed value = 87

# get the baseline data for key 0
mpr.baseline_data(0)
# not pressed value = 348
# pressed value = 316
