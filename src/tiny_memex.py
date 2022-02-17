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
