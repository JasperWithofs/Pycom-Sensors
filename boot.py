import network
import time
import pycom

# setup as a station
wlan = network.WLAN(mode=network.WLAN.STA)
wlan.connect('AFBLIJVEN 1', auth=(network.WLAN.WPA2, 'xxxx'))
while not wlan.isconnected():
    time.sleep_ms(50)
print(wlan.ifconfig())
