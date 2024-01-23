# Teste do sensor de som KY 038

# Importa as bibliotecas
from machine import Pin, ADC
from time import sleep

# Configurar o pino analogico do sensor como uma entrada analogica
analog_pin = ADC(Pin(15))

# Configurar o pino digital do sensor como entrada digital
digital_pin = Pin(14, Pin.IN)

while True:
    # Ler o valor analgico do sensor 
    analog_valor = analog_pin.read()
    
    # Ler o valor digital do sensor
    digital_valor = digital_pin.value()

    # Imprimir o valor na tela
    print('Valor do pino Analogico:', analog_valor, 'Valor do pino Digital:', digital_valor)
    
    # Aguarda 2 segundos
    sleep(2)
