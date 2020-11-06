#!/usr/bin/env python3

from functools import reduce

import serial
import time
import random

ser = serial.Serial('/dev/arduino0')
ser.baudrate = 9600
w = random.choice([b'r', b'g', b'b', b'c', b'm', b'y', b'w'])

print("writing " + str(w))

ser.write(w)
