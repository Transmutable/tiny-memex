# Userspace framebuffer copy to dual displays

Tiny Memex has two PiTFT 240x320 LCDs side-by-side, accessed via SPI0 and SPI1. 
This program copies the left and right half of the Broadcom GPU framebuffer to these displays, 30 times per second.
This means you can use the Broadcom chip's graphics acceleration features (e.g. via X11).

For best quality set the framebuffer resolution to 480x320:

	disable_overscan=1
	hdmi_force_hotplug=1
	hdmi_group=2
	hdmi_mode=87
	hdmi_cvt=480 320 30 1 0 0 0

You can also set a higher resolution (e.g. 960x640) which the GPU will downsample automatically, leading to an anti-aliased image.

## Caveats

This currently does not automatically detect the Pi version. 
It hard-codes the GPIO base address to the Pi4 
(should be same as Pi3 but different from Pi2 or Pi1)

## Credits

This dual driver was created by Vanessa Freudenberg (@codefrau)
based on https://github.com/adafruit/Adafruit_Userspace_PiTFT

Unlike the similar `fbcp` it requires no kernel drivers to talk to the LCD, it uses SPI directly.
