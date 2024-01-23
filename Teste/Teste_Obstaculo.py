# Teste do sensor de Obstaculo Infravermelho

# Importando as bibliotecas
from machine import Pin
import time

# Configurar o pino do sensor obstaculo como uma entrada digital
sensor_pin = Pin(14, Pin.IN)  # pino do sensor

# Configurar o pino do LED como uma saida digital
led_pin = Pin(15, Pin.OUT)  # pino do LED

while True:
    # Ler o valor do sensor de luz
    sensor_value = sensor_pin.value()

    # Se o sensor estiver em estado HIGH, acender o LED
    if sensor_value == 0:
        led_pin.on()  # Ligar o LED
    else: # Seno
        led_pin.off()  # Desligar o LED

    # Imprimir o valor na tela
    print('Valor do Obstaculo:', sensor_value)


    # Aguardar um curto perodo de tempo antes de verificar novamente (evita leituras rpidas)
    time.sleep(0.1)
