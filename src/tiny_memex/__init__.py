import digitalio
import board

CONTROL_PANEL_ADDRESS = 0x20

PLATEN_PINS = [board.D4, board.D27, board.D22]

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

# Control panel input
GRID_ROW_PIN_NUMBERS = [i for i in range(7)]
SOLO_SWITCH_PIN_NUMBER = 7
GRID_COLUMN_PIN_NUMBERS = [i for i in range(8, 13)]
LEVER_LEFT_PIN_NUMBER = 13
LEVER_RIGHT_PIN_NUMBER = 14
EXTRA_INPUT = 15 # Unpopulated to the right of the io expander chip
