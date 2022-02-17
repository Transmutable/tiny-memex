#!/bin/python

import sys
import digitalio
import board
import time
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017
from tiny_memex import CONTROL_PANEL_ADDRESS

def run_test():
    i2c = busio.I2C(board.SCL, board.SDA)
    mcp = MCP23017(i2c, address=CONTROL_PANEL_ADDRESS)
    pins = []
    for index in range(16):
        pin = mcp.get_pin(index)
        pin.direction = digitalio.Direction.INPUT
        pin.pull = digitalio.Pull.UP
        pins.append(pin)
    while True:
        for i in range(16):
            if i % 4 == 0:
                print(" ", end='')
            if pins[i].value == True:
                print('0', end='')
            else:
                print('1', end='')
        print()
        time.sleep(1)

if __name__ == '__main__':
    run_test()


