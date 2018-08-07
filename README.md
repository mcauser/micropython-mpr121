# MicroPython MPR121

MicroPython driver for MPR121 capacitive touch keypads and breakout boards.

![demo](docs/demo.jpg)

![demo](docs/demo2.jpg)

Compatible with:
* [SparkFun Capacitive Touch Keypad - MPR121](https://www.sparkfun.com/products/12017) (discontinued)
* [MPR121 Capacitive Touch Keypad](https://www.aliexpress.com/item/MPR121-capacitive-touch-sensor-module-sensor-keys-keyboard-keys-for-arduino/32810655083.html)
* [MPR121 Capacitive Touch Breakout Board](https://www.aliexpress.com/item/MPR121-Breakout-V12-Capacitive-Touch-Sensor-Controller-Module-I2C-keyboard/32820571887.html)

These boards use 3.3V logic, so you would want to use a logic level converter with this for 5V systems.

## Examples

Copy the file to your device, using ampy, webrepl or compiling and deploying. eg.

```
$ ampy put mpr121.py
```

**Basic usage**

```python
import mpr121

from machine import Pin
i2c = machine.I2C(3)

mpr = mpr121.MPR121(i2c, 0x5A)

print(mpr.touched())
```

For more detailed examples, see [/examples](/examples)

## Parts

* [VCC-GND STM32F407VET6 mini](https://www.aliexpress.com/item/STM32F407VET6-Mini-version-of-the-core-board-STM32-minimum-system-version/32709285751.html) $15.47 AUD
* [MPR121 Capacitive Touch Keypad](https://www.aliexpress.com/item/MPR121-capacitive-touch-sensor-module-sensor-keys-keyboard-keys-for-arduino/32810655083.html) $2.88 AUD
* [Female-Female Dupont wires](https://www.aliexpress.com/item/10pcs-10cm-2-54mm-1p-1p-Pin-Male-to-Male-Color-Breadboard-Cable-Jump-Wire-Jumper/32636873838.html) $0.64 AUD

## Connections

STM32F407VET6 | MPR121 Capacitive Touch Keypad
------------- | -----------------
3V3 (or 5V)   | VCC
D3 (any pin)  | IRQ
A8 (SPI3 SCL) | SCL
C9 (SPI3 SDA) | SDA
GND           | GND

## Links

* [micropython.org](http://micropython.org)
* [MPR121 datasheet](http://micropython.org/resources/datasheets/MPR121.pdf)
* [MPR121 product page](https://www.nxp.com/products/no-longer-manufactured/proximity-capacitive-touch-sensor-controller:MPR121)
* [Adafruit Ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy)

## License

Licensed under the [MIT License](http://opensource.org/licenses/MIT).
