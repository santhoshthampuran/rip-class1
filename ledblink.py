from gpiozero import LED
from time import sleep

led = LED(17)
print("setting to GPIO 17...")

count=0

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    print("cycle {0}".format(count))
    count +=1
