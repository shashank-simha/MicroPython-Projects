import network 
import machine

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True) 
sta_if.connect("Redmi Y1", "123454321")
sta_if.isconnected()
sta_if.ifconfig()

ap = network.WLAN(network.AP_IF)
ap.active(True)

ap.config(essid='ESP32-AP', authmode=3, password="12345678") 

stations=ap.status('stations')s
