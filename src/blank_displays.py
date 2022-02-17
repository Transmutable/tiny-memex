#!/usr/bin/python3

import sys
import digitalio
import board
import time
import busio
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import ili9341

from tiny_memex import LEFT_SPI, RIGHT_SPI, SPI_BAUDRATE

def make_display(sck, mosi, miso, dc, cs):
    spi = busio.SPI(sck, mosi, miso)
    disp = ili9341.ILI9341(spi, rotation=0, cs=cs, dc=dc, baudrate=SPI_BAUDRATE)
    return (spi, disp)

(left_spi, left_disp) = make_display(LEFT_SPI["sck"], LEFT_SPI["mosi"], LEFT_SPI["miso"], LEFT_SPI["dc"], LEFT_SPI["cs"])
width = left_disp.width
height = left_disp.height
left_image = Image.new("RGB", (width, height))
left_draw = ImageDraw.Draw(left_image)

(right_spi, right_disp) = make_display(RIGHT_SPI["sck"], RIGHT_SPI["mosi"], RIGHT_SPI["miso"], RIGHT_SPI["dc"], RIGHT_SPI["cs"])
right_image = Image.new("RGB", (width, height))
right_draw = ImageDraw.Draw(right_image)

def blank(draw, display, image):
    draw.rectangle((0, 0, width, height), fill=(0,0,0))
    display.image(image)    

if __name__ == '__main__':
    blank(left_draw, left_disp, left_image)
    blank(right_draw, right_disp, right_image)
 

