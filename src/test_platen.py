#!/usr/bin/python3

import time
import board
import digitalio
from tiny_memex import PLATEN_PINS

left_button = digitalio.DigitalInOut(PLATEN_PINS[0])
left_button.direction = digitalio.Direction.INPUT
left_button.pull = digitalio.Pull.UP

middle_button = digitalio.DigitalInOut(PLATEN_PINS[1])
middle_button.direction = digitalio.Direction.INPUT
middle_button.pull = digitalio.Pull.UP

right_button = digitalio.DigitalInOut(PLATEN_PINS[2])
right_button.direction = digitalio.Direction.INPUT
right_button.pull = digitalio.Pull.UP

while True:
    print(left_button.value, middle_button.value, right_button.value)
    time.sleep(1)

