#!/usr/bin/python3

import board
import digitalio
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017
from tiny_memex import LEFT_SPI, RIGHT_SPI, CONTROL_PANEL_ADDRESS

# This script tests whether Python can connect to the inputs via I2C and the displays via SPI
# usage: ~/tiny-memex/src/test_blinka.py

print("Testing  IO: ", end='')
pin = digitalio.DigitalInOut(board.D4)
print("OK")

print("Testing I2C: ", end='')
i2c = busio.I2C(board.SCL, board.SDA)
print("OK")

print("Testing control panel: ", end='')
mcp = MCP23017(i2c, address=CONTROL_PANEL_ADDRESS)
pin = mcp.get_pin(0)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP
if pin.value == 1:
	print("OK")
else:
	print("FAIL")

print("Testing Left SPI 0: ", end='')
spi0 = busio.SPI(LEFT_SPI['sck'], LEFT_SPI['mosi'], LEFT_SPI['miso'])
print("OK")

print("Testing Right SPI 1: ", end='')
spi1 = busio.SPI(RIGHT_SPI['sck'], RIGHT_SPI['mosi'], RIGHT_SPI['miso'])
print("OK")
