from machine import Pin
import time

p2 = Pin(2, Pin.OUT)

while True:
	p2.value(1)
	print("On\n")
	time.sleep(1)
	p2.value(0)
	print("Off\n")
	time.sleep(1)
