import pcd8544
import framebuf
import utime
import machine
import _thread

from machine import Pin, SPI

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

framebuf.fill(0)
lcd.data(buffer)

framebuf.text("Hello", 22, 16, 1)
framebuf.text("World", 22, 26, 1)
lcd.data(buffer)

