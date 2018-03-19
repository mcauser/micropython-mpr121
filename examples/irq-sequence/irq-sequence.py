"""
The password is 4567.
Enter the correct password to unlock the pretend door.
"""

import mpr121
from machine import Pin

i2c = machine.I2C(3)
mpr = mpr121.MPR121(i2c)

password = [4,5,6,7]
position = 0

last = 0

def check(pin):
    global last
    global password
    global position
    touched = mpr.touched()
    diff = last ^ touched
    for i in range(12):
        if diff & (1 << i):
            if not touched & (1<<i):
                print('Key {} released'.format(i))
                if i == password[position]:
                    position += 1;
                    # print("*" * position)
                else:
                    position = 0;
                    # print("reset")
                if position == len(password):
                    print("Password correct. Door unlocked.")
                    position = 0;
    last = touched

d3 = Pin('D3', Pin.IN, Pin.PULL_UP)
d3.irq(check, Pin.IRQ_FALLING)
