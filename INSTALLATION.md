# Tiny Memex Installation

These instructions are for the 64 bit version of Raspberry Pi OS Lite released on January 28th 2022 running on a Raspberry Pi 4 B.


## Raspberry OS configuration

### Edit files on the SD card

On your PC, use the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) to write the 64-bit Lite image to your SD card.

The remove and re-insert the SD card and in the root of the boot drive that appears:

Create an empty file:

	cd <path to boot drive>
	touch ./ssh

If you want to use WiFi instead of Ethernet then in the same directory create a 'wpa_supplicant.conf' file containing this: 

country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
scan_ssid=1
ssid="your_wifi_ssid"
psk="your_wifi_password"
}

Now eject the SD card, insert it into the Raspberry Pi, and insert the USB-C power cable. If you're using Ethernet then insert that cable, too.

Wait a couple of minutes, then ping 'raspberrypi' or 'raspberrypi.local' until you get a response. Once it returns pings, ssh into your Tiny Memex:

	ssh pi@raspberrypi # the username is 'raspberry'

Once you're connected it's time to become root and set up the base software:

	sudo su -
	apt update
	apt -y upgrade

Run the Raspberry Pi OS configurator:

	raspi-config

Use the menus to set your password. (Trevor always uses 'vannevar')

Use the menus to set the hostname to 'tinymemex-??' where ?? is your serial number (01 through 20). For the rest of this document we'll use 'tinymemex-01' but be sure to use your hostname.

Use the menus to enable SPI.

Use the menus to enable I2C.

Use the menus to enable SSH.

Exit raspi-config.

Add a new line to the bottom of '/boot/config.txt' that contains `dtoverlay=spi1-3cs` (no quotes).

Reboot:

	shutdown -r now

Wait a couple of minutes then ssh back in and become root:

	ssh pi@tinymemex-01 # remember to use your new hostname and password
	sudo su -

As root, run the following commands:

	apt install -y git python3-pip
	pip install --upgrade -y setuptools adafruit-python-shell
	wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
	python raspi-blinka.py # this takes a few minutes
	rm raspi-blinka.py

Reboot again (`shutdown -r now`), wait, ssh in, and become root with `sudo su -`.

As root, run:

	pip install adafruit-circuitpython-mcp230xx adafruit-circuitpython-ili9341 adafruit-circuitpython-rgb-display click

Edit '/usr/local/lib/python3.9/dist-packages/adafruit_blinka/microcontroller/bcm2711/pin.py' and search for 'spiPorts'. In that section make the following change:

Original:
(6, SCLK_1, MOSI_1, MISO_1),

Change it to:
(1, SCLK_1, MOSI_1, MISO_1),

Now go back to being 'pi' by exiting the root shell: `exit`

## Get the Tiny Memex example service and Python code

As the pi account (not root):

	cd # takes you to your home directory at '/home/pi/'
	git clone https://github.com/Transmutable/tiny-memex.git
