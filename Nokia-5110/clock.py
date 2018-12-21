import pcd8544
import framebuf
import utime
import machine
import _thread
import wifiConnect
from machine import Pin, SPI

wifiConnect.connect()

#set ntp time
from ntptime import settime 
settime()

def getDateTime():
	t = utime.localtime()
	y, m, d, h, mi, s = t[0], t[1], t[2], t[3], t[4], t[5]

	y = str(y)

	if(m<10):
		m = "0" + str(m)
	else:
		m = str(m)
		 	
	if(d<10):
		d = "0" + str(d)
	else:
		d = str(d)

	if(h<10):
		h = "0" + str(h)
	else:
		h = str(h)

	if(mi<10):
		mi = "0" + str(mi)
	else:
		mi = str(mi)

	if(s<10):
		s = "0" + str(s)
	else:
		s = str(s)
	
	date = d + "-" + m  + "-" + y
	time = h + ":" + mi + ":" + s
	
	return date, time
	
sckPin = Pin(18)
mosiPin = Pin(23)
misoPin = Pin(19)

spi = SPI(1, baudrate=328125, bits=8, polarity=0, phase=1, sck=sckPin, mosi=mosiPin, miso=misoPin)
spi.init()

cs = Pin(2)
dc = Pin(15)
rst = Pin(0)

# backlight on
bl = Pin(12, Pin.OUT, value=1)

lcd = pcd8544.PCD8544(spi, cs, dc, rst)
lcd.contrast(0x3c, pcd8544.BIAS_1_40, pcd8544.TEMP_COEFF_0)
lcd.reset()
lcd.init()
lcd.clear()


buffer = bytearray((lcd.height // 8) * lcd.width)
framebuf = framebuf.FrameBuffer1(buffer, lcd.width, lcd.height)

while True:
	framebuf.fill(0)
	lcd.data(buffer)
	date, time = getDateTime()
	framebuf.text(date, 3, 16, 1)
	framebuf.text(time, 10, 26, 1)
	lcd.data(buffer)
	utime.sleep(1)

