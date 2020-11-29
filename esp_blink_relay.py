# Complete project details at https://RandomNerdTutorials.com

from machine import Pin
from time import sleep


# ESP8266 GPIO 1
PIN = 5
relay = Pin(PIN, Pin.OUT)
print("Iniciando")

while True:
  # RELAY ON
  print("Apagado")
  relay.value(0)
  sleep(1)
  # RELAY OFF
  print("Prendido")
  relay.value(1)
  sleep(1)
