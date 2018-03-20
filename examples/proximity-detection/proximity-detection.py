"""
Enable proximity detection.
It works, but is very noisy. Registers need tweaking.
"""

import mpr121
from machine import Pin

i2c = machine.I2C(3)
mpr = mpr121.MPR121(i2c)

# the 13th electrode is the proximity channel

# constants not in the driver (yet)
MPR121_PROX_MAX_HALF_DELTA_RISING = const(0x36) # Max half delta (rising)
MPR121_PROX_NOISE_HALF_DELTA_RISING = const(0x37) # Noise half delta (rising)
MPR121_PROX_NOISE_COUNT_LIMIT_RISING = const(0x38) # Noise count limit (rising)
MPR121_PROX_FILTER_DELAY_COUNT_RISING = const(0x39) # Filter delay count (rising)
MPR121_PROX_MAX_HALF_DELTA_FALLING = const(0x3A) # Max half delta (falling)
MPR121_PROX_NOISE_HALF_DELTA_FALLING = const(0x3B) # Noise half delta (falling)
MPR121_PROX_NOISE_COUNT_LIMIT_FALLING = const(0x3C) # Noise count limit (falling)
MPR121_PROX_FILTER_DELAY_COUNT_FALLING = const(0x3D) # Filter delay count (falling)
# There is no max half delta for touched
MPR121_PROX_NOISE_HALF_DELTA_TOUCHED = const(0x3E) # Noise half delta (touched)
MPR121_PROX_NOISE_COUNT_LIMIT_TOUCHED = const(0x3F) # Noise count limit (touched)
MPR121_PROX_FILTER_DELAY_COUNT_TOUCHED = const(0x40) # Filter delay count (touched)


# enter stop mode
mpr._register8(mpr121.MPR121_ELECTRODE_CONFIG, 0x00)

# duplicate electrode config to proximity registers
mpr._register8(MPR121_PROX_MAX_HALF_DELTA_RISING, 0x01)
mpr._register8(MPR121_PROX_MAX_HALF_DELTA_FALLING, 0x01)
mpr._register8(MPR121_PROX_NOISE_HALF_DELTA_RISING, 0x01)
mpr._register8(MPR121_PROX_NOISE_HALF_DELTA_FALLING, 0x05)
mpr._register8(MPR121_PROX_NOISE_HALF_DELTA_TOUCHED, 0x00)
mpr._register8(MPR121_PROX_NOISE_COUNT_LIMIT_RISING, 0x0E)
mpr._register8(MPR121_PROX_NOISE_COUNT_LIMIT_FALLING, 0x01)
mpr._register8(MPR121_PROX_NOISE_COUNT_LIMIT_TOUCHED, 0x00)
mpr._register8(MPR121_PROX_FILTER_DELAY_COUNT_RISING, 0x00)
mpr._register8(MPR121_PROX_FILTER_DELAY_COUNT_FALLING, 0x00)
mpr._register8(MPR121_PROX_FILTER_DELAY_COUNT_TOUCHED, 0x00)

# set thresholds (13th electrode = proximity)
mpr._register8(mpr121.MPR121_TOUCH_THRESHOLD + 13 * 2, 15)
mpr._register8(mpr121.MPR121_RELEASE_THRESHOLD + 13 * 2, 7)

# max debounce touch and release to reduce noise
mpr._register8(mpr121.MPR121_DEBOUNCE, 0x77)

# enter run mode with proximity enabled (0x30) on all electrodes (0x0F)
mpr._register8(mpr121.MPR121_ELECTRODE_CONFIG, 0x80 | 0x30 | 0x0F)
mpr.touched()

# check all keys
def check(pin):
    print(mpr.touched())

d3 = Pin('D3', Pin.IN, Pin.PULL_UP)
d3.irq(check, Pin.IRQ_FALLING)
