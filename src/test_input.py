#!/usr/bin/python3

import sys
import time
from tiny_memex import TinyMemex

# This script repeatedly prints true or false for each button and the lever switch
# usage: ~/tiny-memex/src/test_input.py

def run_test():
	memex = TinyMemex()

	while True:
		memex.read_control_panel()
		memex.print_control_panel_grid()
		print(memex.control_panel_bottom_button, memex.control_panel_left_lever, memex.control_panel_right_lever)
		memex.read_platen()
		print(memex.platen_left_button, memex.platen_middle_button, memex.platen_right_button)
		print()
		time.sleep(1)

if __name__ == '__main__':
	run_test()


