# Teste do sensor LDR Micropython

# Importa as bibliotecas
from machine import Pin, ADC
import time

# Configurar o pino do sensor LDR como uma entrada analogica
ldr_pin = ADC(Pin(A0))

# Configurar o pino do LED como uma sada digital
led_pin = Pin(2, Pin.OUT)

while True:
    # Ler o valor analgico do sensor LDR
    ldr_value = ldr_pin.read()

    # Se o valor lido for maior que 200, acender o LED
    if ldr_value > 200:
        led_pin.on  # Ligar o LED
    # Senao
    else:
        led_pin.off  # Desligar o LED

    # Imprimir o valor na tela
    print('Valor do pino Analogico:', analog_valor)

    # Aguarda 2 segundos
    time.sleep(2)
