#!/usr/bin/python3

from PIL import ImageDraw

from tiny_memex import TinyMemex

# This script clears the displays by drawing black rectangles
# usage: ~/tiny-memex/src/blank_displays.py

memex = TinyMemex()
left_draw = ImageDraw.Draw(memex.left_image)
right_draw = ImageDraw.Draw(memex.right_image)

def blank(draw, display, image):
    draw.rectangle((0, 0, display.width, display.height), fill=(0,0,0))
    display.image(image)    

if __name__ == '__main__':
    blank(left_draw, memex.left_display, memex.left_image)
    blank(right_draw, memex.right_display, memex.right_image)
