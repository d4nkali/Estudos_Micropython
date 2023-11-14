# Programa Piscar led

# Importa as bibliotecas
import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # Define o pino GPIO2 como do LED da placa

while True: # Cria um loop
    led.value(not led.value()) # Alterna os valores entre ligado e desligado
    time.sleep(1) # Aguarda 1 segundo
