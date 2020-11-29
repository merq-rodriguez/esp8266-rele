# Complete project details at https://RandomNerdTutorials.com

try:
    import gc
    import usocket as socket
except:
    import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

gc.collect()

SSID = 'ssid'
PASSWORD = 'password'

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)

        while not sta_if.isconnected():
            print("Conecting...")
    print('network config:', sta_if.ifconfig())
    return sta_if.ifconfig()

print('Connection successful')
config = do_connect()
print(config)


# ESP8266 GPIO 1
D1 = 1
relay = Pin(D1, Pin.OUT)
