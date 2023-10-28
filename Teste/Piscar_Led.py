import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # GPIO2 o pino do LED da placa

while True:
    led.value(not led.value())
    time.sleep(1)
