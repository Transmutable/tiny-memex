#!/usr/bin/python3

import time
import array
import fcntl
import socket
import struct
import socket
import datetime
from PIL import ImageDraw, ImageFont

from tiny_memex import TinyMemex

memex = TinyMemex()
left_draw = ImageDraw.Draw(memex.left_image)
right_draw = ImageDraw.Draw(memex.right_image)

time_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 48)
time_color = (255, 128, 128) 

host_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
host_color = (128, 128, 255)


def blank(draw, display, image):
	draw.rectangle((0, 0, display.width, display.height), fill=(0,0,0))
	display.image(image)    

def write(draw, display, image, text, font, color):
	draw.rectangle((0, 0, display.width, display.height), fill=(0,0,0))
	(font_width, font_height) = font.getsize(text)
	draw.text(
		(display.width // 2 - font_width // 2, display.height // 2 - font_height // 2),
		text,
		font=font,
		fill=color,
	)
	display.image(image)    

def get_hostname_and_ip():
	host_name = socket.gethostname()
	return (host_name, socket.gethostbyname(host_name))


def get_local_interfaces():
	""" Returns a dictionary of name:ip key value pairs. """
	MAX_BYTES = 4096
	FILL_CHAR = b'\0'
	SIOCGIFCONF = 0x8912
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	names = array.array('B', MAX_BYTES * FILL_CHAR)
	names_address, names_length = names.buffer_info()
	mutable_byte_buffer = struct.pack('iL', MAX_BYTES, names_address)
	mutated_byte_buffer = fcntl.ioctl(sock.fileno(), SIOCGIFCONF, mutable_byte_buffer)
	max_bytes_out, names_address_out = struct.unpack('iL', mutated_byte_buffer)
	namestr = names.tobytes()
	namestr[:max_bytes_out]
	bytes_out = namestr[:max_bytes_out]
	ip_dict = {}
	for i in range(0, max_bytes_out, 40):
		name = namestr[ i: i+16 ].split(FILL_CHAR, 1)[0]
		name = name.decode('utf-8')
		ip_bytes   = namestr[i+20:i+24]
		full_addr = []
		for netaddr in ip_bytes:
			if isinstance(netaddr, int):
				full_addr.append(str(netaddr))
			elif isinstance(netaddr, str):
				full_addr.append(str(ord(netaddr)))
		ip_dict[name] = '.'.join(full_addr)

	return ip_dict

def get_local_ip_address():
	for interface, ip in get_local_interfaces().items():
		if ip.startswith("127.") == False:
			return ip
	return None

blank(left_draw, memex.left_display, memex.left_image)
blank(right_draw, memex.right_display, memex.right_image)

for iface, ip in get_local_interfaces().items():
	print("{ip:15s} {iface}".format(ip=ip, iface=iface))

left_text = ""
right_text = ""
frame_index = 0
while True:
	frame_index = (frame_index + 1) % 10
	dt = datetime.datetime.now()
	new_left_text = "%02i:%02i" % (dt.hour, dt.minute)

	if frame_index > 4:
		new_right_text = "%s" % socket.gethostname()
	else:
		ip_address = get_local_ip_address()
		new_right_text = "%s" % ip_address

	if left_text != new_left_text:
		left_text = new_left_text
		write(left_draw, memex.left_display, memex.left_image, left_text, time_font, time_color)
	if right_text != new_right_text:
		right_text = new_right_text
		write(right_draw, memex.right_display, memex.right_image, right_text, host_font, host_color)
	time.sleep(1)
