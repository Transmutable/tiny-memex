#!/usr/bin/python3

import sys
from PIL import ImageDraw, ImageFont

from tiny_memex import TinyMemex

FONTSIZE = 48

memex = TinyMemex()
left_draw = ImageDraw.Draw(memex.left_image)
right_draw = ImageDraw.Draw(memex.right_image)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)
text_color = 255 

def write(draw, display, image, text):
	draw.rectangle((0, 0, display.width, display.height), fill=(0,0,0))
	(font_width, font_height) = font.getsize(text)
	draw.text(
		(display.width // 2 - font_width // 2, display.height // 2 - font_height // 2),
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
	write(left_draw, memex.left_display, memex.left_image, left_text)
	write(right_draw, memex.right_display, memex.right_image, right_text)
