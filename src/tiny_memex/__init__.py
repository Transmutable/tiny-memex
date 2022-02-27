import sys
import busio
import board
import digitalio
from PIL import Image
from adafruit_rgb_display import ili9341
from adafruit_mcp230xx.mcp23017 import MCP23017 # Control panel IO expander chip accessed via I2C

SPI_BAUDRATE = 24000000

LEFT_SPI = {
	"cs": digitalio.DigitalInOut(board.CE0),
	"dc": digitalio.DigitalInOut(board.D25),
	"mosi": board.MOSI,
	"miso": board.MISO,
	"sck": board.SCK
}

RIGHT_SPI = {
	"cs": digitalio.DigitalInOut(board.D16),
	"dc": digitalio.DigitalInOut(board.D26),
	"mosi": board.MOSI_1,
	"miso": board.MISO_1,
	"sck": board.SCK_1
}

CONTROL_PANEL_ADDRESS = 0x20 # The I2C address for the MCP23017

PLATEN_PINS = [board.D4, board.D27, board.D22]

CONTROL_PANEL_ROW_COUNT = 7
CONTROL_PANEL_COLUMN_COUNT = 5

# Control panel IO pins
GRID_ROW_PIN_NUMBERS = [i for i in range(7)]
BOTTOM_SWITCH_PIN_NUMBER = 7
GRID_COLUMN_PIN_NUMBERS = [i for i in range(8, 13)]
LEVER_LEFT_PIN_NUMBER = 13
LEVER_RIGHT_PIN_NUMBER = 14
EXTRA_INPUT_PIN_NUMBER = 15 # Unpopulated to the right of the io expander chip

def make_display(sck, mosi, miso, dc, cs):
	spi = busio.SPI(sck, mosi, miso)
	disp = ili9341.ILI9341(spi, rotation=0, cs=cs, dc=dc, baudrate=SPI_BAUDRATE)
	return (spi, disp)

def setup_input_pin(pin):
	pin.direction = digitalio.Direction.INPUT
	pin.pull = digitalio.Pull.UP

class TinyMemex:
	def __init__(self):
		(self.left_spi, self.left_display) = make_display(LEFT_SPI["sck"], LEFT_SPI["mosi"], LEFT_SPI["miso"], LEFT_SPI["dc"], LEFT_SPI["cs"])
		self.left_image = Image.new("RGB", (self.left_display.width, self.left_display.height))

		(self.right_spi, self.right_display) = make_display(RIGHT_SPI["sck"], RIGHT_SPI["mosi"], RIGHT_SPI["miso"], RIGHT_SPI["dc"], RIGHT_SPI["cs"])
		self.right_image = Image.new("RGB", (self.right_display.width, self.right_display.height))

		# These values are updated by TinyMemex.read_platen
		self.platen_left_button = False
		self.platen_middle_button = False
		self.platen_right_button = False

		self.platen_left_pin = digitalio.DigitalInOut(PLATEN_PINS[0])
		setup_input_pin(self.platen_left_pin)
		self.platen_middle_pin = digitalio.DigitalInOut(PLATEN_PINS[1])
		setup_input_pin(self.platen_middle_pin)
		self.platen_right_pin = digitalio.DigitalInOut(PLATEN_PINS[2])
		setup_input_pin(self.platen_right_pin)

		# These values are updated by TinyMemex.read_control_panel
		self.control_panel_rows = [[False, False, False, False, False] for n in range(CONTROL_PANEL_ROW_COUNT)] # an array of row value arrays
		self.control_panel_left_lever = False
		self.control_panel_right_lever = False
		self.control_panel_bottom_button = False

		self.control_panel_bus = busio.I2C(board.SCL, board.SDA)
		self.control_panel_chip = MCP23017(self.control_panel_bus, address=CONTROL_PANEL_ADDRESS)

		self.control_panel_row_pins = []
		for index in GRID_ROW_PIN_NUMBERS:
			pin = self.control_panel_chip.get_pin(index)
			pin.direction = digitalio.Direction.INPUT
			self.control_panel_row_pins.append(pin)

		self.control_panel_column_pins = []
		for index in GRID_COLUMN_PIN_NUMBERS:
			pin = self.control_panel_chip.get_pin(index)
			pin.direction = digitalio.Direction.OUTPUT
			pin.value = 0
			self.control_panel_column_pins.append(pin)

		self.control_panel_bottom_button_pin = self.control_panel_chip.get_pin(BOTTOM_SWITCH_PIN_NUMBER)
		setup_input_pin(self.control_panel_bottom_button_pin)
		self.control_panel_lever_left_pin = self.control_panel_chip.get_pin(LEVER_LEFT_PIN_NUMBER)
		setup_input_pin(self.control_panel_lever_left_pin)
		self.control_panel_lever_right_pin = self.control_panel_chip.get_pin(LEVER_RIGHT_PIN_NUMBER)
		setup_input_pin(self.control_panel_lever_right_pin)

	def read_control_panel(self):
		for column_index, column_pin in enumerate(self.control_panel_column_pins):
			column_pin.value = 1
			for row_index, row_pin in enumerate(self.control_panel_row_pins):
				self.control_panel_rows[row_index][column_index] = row_pin.value
			column_pin.value = 0

		self.control_panel_bottom_button = self.control_panel_bottom_button_pin.value == False
		self.control_panel_left_lever = self.control_panel_lever_left_pin.value == False
		self.control_panel_right_lever = self.control_panel_lever_right_pin.value == False

	def read_platen(self):
		self.platen_left_button = self.platen_left_pin.value == False
		self.platen_middle_button = self.platen_middle_pin.value == False
		self.platen_right_button = self.platen_right_pin.value == False

	def print_control_panel_grid(self):
		for row_index in range(CONTROL_PANEL_ROW_COUNT):
			for column_index in range(CONTROL_PANEL_COLUMN_COUNT):
				print(self.control_panel_rows[row_index][column_index], end=' ')
			print()



