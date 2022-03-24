# Remote Access via SSH

You can log into your Tiny Memex remotely via Ethernet or Wifi.

Ethernet works out of the box. For Wifi you either plug in a screen and keyboard and use the Raspberry Pi's config app, or you edit the config files directly on the SD card using another computer.

## Ethernet

Plug it in. Continue below.

## Wifi Method 1: Screen and Keyboard

You need:
* a Micro HDMI cable or adapter (!)
* an HDMI monitor
* a USB keyboard

Connect the screen to the Raspberry PI using Micro HDMI. Plug in the USB keyboard.

You should see a login, the password is "`vannevar`".

Run the Raspberry Pi OS configurator:

    raspi-config

Use the menu to connecto to Wifi.

## Wifi Method 2: Edit files on the SD card

You need:
* a computer
* an adapter for micro SD cards

Insert the SD card and in the root of the boot drive that appears create a `wpa_supplicant.conf` file containing this:

	country=US
	ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
	update_config=1

	network={
		scan_ssid=1
		ssid="your_wifi_ssid"
		psk="your_wifi_password"
	}

Now eject the SD card, and insert it into the Raspberry Pi.

# Logging in

Insert the USB-C power supply and switch it on. The green and red LEDs inside the case should start blinking.

Wait until the right screen of your Tiny Memex shows an IP address in addition to the host name ("`tinymemex-??`" where "`??`" is your serial number).

Assuming the IP address is `192.168.1.2` then ssh into your Tiny Memex:

	ssh pi@192.168.1.2         # the password is 'vannevar'

Alternatively you can use "`tinymemex-??`" or "`tinymemex-??.local`" instead of the IP address.
