
import mpr121
from machine import Pin

i2c = machine.I2C(3)
mpr = mpr121.MPR121(i2c)

# get the filtered data for key 0
mpr.filtered_data(0)
# not pressed value = 350
# pressed value = 87

# get the baseline data for key 0
mpr.baseline_data(0)
# not pressed value = 348
# pressed value = 316
