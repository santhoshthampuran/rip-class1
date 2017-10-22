from gpiozero import LED
from time import sleep


# blinking function
def blink(pin, times=None):
	led = LED(pin)
	print("setting to GPIO 17...")
	print (times)
	for i in range(0, times):
		led.on()
		sleep(1)
		led.off()
		sleep(1)
		print("cycle {0}".format(i))


blink(17, 5)
