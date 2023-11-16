# Teste do led RGB

# Importa as bibliotecas
import machine
import time

vermelho = machine.Pin(14, machine.Pin.OUT)  # Define o pino GPIO14 como do pino vermelho do LED RGB
verde = machine.Pin(12, machine.Pin.OUT)  # Define o pino GPIO12 como do pino verde do LED RGB
azul = machine.Pin(13, machine.Pin.OUT)  # Define o pino GPIO2 como do pino azul LED RGB 

while True: # Cria um loop
    vermelho.value(not led.value()) # Alterna os valores entre ligado e desligado
    time.sleep(1) # Aguarda 1 segundo
    verde.value(not led.value()) # Alterna os valores entre ligado e desligado
    time.sleep(1) # Aguarda 1 segundo
    azul.value(not led.value()) # Alterna os valores entre ligado e desligado
    time.sleep(1) # Aguarda 1 segundo
    