from gpiozero import LED
from time import sleep
import logger

log = logger.getLogger(__name__, False)


# blinking function
def blink(pin, times=None):
	led = LED(pin)
	log.info("setting to GPIO pin 17...")
	log.info("Start blinking %d times", times)

	for i in range(0, times):
		led.on()
		sleep(1)
		led.off()
		sleep(1)
		log.info("cycle %d", i)
