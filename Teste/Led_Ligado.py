# Programa Led Ligado

# Importa as bibliotecas
import machine

led = machine.Pin(2, machine.Pin.OUT)  # Define o pino GPIO2 como do LED da placa
led.value(1) # Liga o led