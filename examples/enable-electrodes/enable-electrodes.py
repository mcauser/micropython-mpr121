"""
Enable 0-n electrodes.
"""

import mpr121
from machine import Pin

i2c = machine.I2C(3)
mpr = mpr121.MPR121(i2c)

# get the current config
print(mpr._register8(mpr121.MPR121_ELECTRODE_CONFIG)) # 143 (0x8F)

# low 4 bits control which electrodes are enabled 0-11 (0000~11xx)

# enable key 0 only
mpr._register8(mpr121.MPR121_ELECTRODE_CONFIG, 0x00) # enter stop mode
mpr._register8(mpr121.MPR121_ELECTRODE_CONFIG, 0x80 | 0x01) # enter run mode
mpr.touched()

# enable keys 0-3
mpr._register8(mpr121.MPR121_ELECTRODE_CONFIG, 0x00) # enter stop mode
mpr._register8(mpr121.MPR121_ELECTRODE_CONFIG, 0x80 | 0x04) # enter run mode
mpr.touched()

# enable keys 0-7
mpr._register8(mpr121.MPR121_ELECTRODE_CONFIG, 0x00) # enter stop mode
mpr._register8(mpr121.MPR121_ELECTRODE_CONFIG, 0x80 | 0x08) # enter run mode
mpr.touched()

# enable keys 0-11
mpr._register8(mpr121.MPR121_ELECTRODE_CONFIG, 0x00) # enter stop mode
mpr._register8(mpr121.MPR121_ELECTRODE_CONFIG, 0x80 | 0x0F) # enter run mode
mpr.touched()
