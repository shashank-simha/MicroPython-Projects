import network

 
def connect():
  ssid = "Redmi Y1"
  password =  "123454321"
 
  station = network.WLAN(network.STA_IF)
 
  if station.isconnected() == True:
      print("Already connected")
      return station.ifconfig()
 
  station.active(True)
  station.connect(ssid, password)
 
  while station.isconnected() == False:
      pass
 
  print("Connection successful")
  print(station.ifconfig())
  return station.ifconfig()
