"""
Compare the filtered data, baseline data and touch detection, with ansi colours
"""

import mpr121
import time
from machine import Pin, I2C

i2c = I2C(3) # stm32
#i2c = I2C(scl=Pin(5), sda=Pin(4)) # esp8266
#i2c = I2C(scl=Pin(22), sda=Pin(21)) # esp32

mpr = mpr121.MPR121(i2c)

#mpr.set_thresholds(15,7)
#mpr.set_thresholds(31,7)
#mpr.set_thresholds(63,15)

red = "\x1B[31;40m"
green = "\x1B[32;40m"
reset = "\x1B[0m"

last_filtered = [mpr.filtered_data(i) for i in range(12)]
last_baseline = [mpr.baseline_data(i) for i in range(12)]
last_touched = [mpr.is_touched(i) for i in range(12)]

filtered = [0] * 12
baseline = [0] * 12
touched = [False] * 12

# header row
print("\t\t" + "\t".join("key"+str(x) for x in range(12)))

def print_table():
    for i in range(12):
        d = mpr.filtered_data(i)
        if d > last_filtered[i]:
            filtered[i] = red
        elif d < last_filtered[i]:
            filtered[i] = green
        else:
            filtered[i] = reset
        filtered[i] += str(d) + reset
        last_filtered[i] = d

        d = mpr.baseline_data(i)
        if d > last_baseline[i]:
            baseline[i] = red
        elif d < last_baseline[i]:
            baseline[i] = green
        else:
            baseline[i] = reset
        baseline[i] += str(d) + reset
        last_baseline[i] = d

        d = mpr.is_touched(i)
        if d:
            touched[i] = green
        else:
            touched[i] = red
        touched[i] += str(d) + reset
        last_touched[i] = d

    print("-"*109)
    print("Filtered\t" + "\t".join(filtered))
    print("Baseline\t" + "\t".join(baseline))
    print("Touched\t\t" + "\t".join(touched))

while True:
    print_table()
    time.sleep_ms(1000)
