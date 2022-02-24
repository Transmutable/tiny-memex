#!/usr/bin/python3

import sys
import digitalio
import board
import time
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017
from tiny_memex import CONTROL_PANEL_ADDRESS, GRID_ROW_PIN_NUMBERS, SOLO_SWITCH_PIN_NUMBER, GRID_COLUMN_PIN_NUMBERS, LEVER_LEFT_PIN_NUMBER, LEVER_RIGHT_PIN_NUMBER

grid_rows = [[0, 0, 0, 0, 0] for n in range(7)] # an array of row value arrays

def print_grid():
    for row_index in range(7):
        for column_index in range(5):
            print(grid_rows[row_index][column_index], end=' ')
        print()

def run_test():
    i2c = busio.I2C(board.SCL, board.SDA)
    mcp = MCP23017(i2c, address=CONTROL_PANEL_ADDRESS)

    row_pins = []
    for index in GRID_ROW_PIN_NUMBERS:
        pin = mcp.get_pin(index)
        pin.direction = digitalio.Direction.INPUT
        # pin.pull = digitalio.Pull.UP
        row_pins.append(pin)

    column_pins = []
    for index in GRID_COLUMN_PIN_NUMBERS:
        pin = mcp.get_pin(index)
        pin.direction = digitalio.Direction.OUTPUT
        pin.value = 0
        column_pins.append(pin)

    while True:
        for column_index, column_pin in enumerate(column_pins):
            column_pin.value = 1
            for row_index, row_pin in enumerate(row_pins):
                grid_rows[row_index][column_index] = row_pin.value
            column_pin.value = 0

        print_grid()
        print()
        time.sleep(0.1)

if __name__ == '__main__':
    run_test()


