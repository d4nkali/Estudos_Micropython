# Piscar led no MicroPython

# Importa as bibliotecas
import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # Define o GPIO2 como o pino do LED da placa em sada

while True: # Loop
    led.value(not led.value()) # Liga e desliga o led
    time.sleep(1) # Aguarda 1 segundo
