#!/bin/python

import sys
import digitalio
import board
import time
import busio
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import ili9341

from tiny_memex import LEFT_SPI, RIGHT_SPI, SPI_BAUDRATE

FONTSIZE = 48

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

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)
text_color = 255 

def write(draw, display, image, text):
	draw.rectangle((0, 0, width, height), fill=(0,0,0))
	(font_width, font_height) = font.getsize(text)
	draw.text(
		(width // 2 - font_width // 2, height // 2 - font_height // 2),
		text,
		font=font,
		fill=(255, 255, 255),
	)
	display.image(image)    


if __name__ == '__main__':
	if len(sys.argv) > 2:
		left_text = sys.argv[1]
		right_text = sys.argv[2]
	else:
		left_text = "Tiny"
		right_text = "Memex"
	write(left_draw, left_disp, left_image, left_text)
	write(right_draw, right_disp, right_image, right_text)
