# Teste do sensor de temperatura e humidade DHT11

# Importa as bibliotecas
from machine import Pin
from time import sleep
import dht

# Configurar o pino GPIO 14 (D5) como do sensor DHT11
sensor = dht.DHT11(Pin(14))

while True:
    sleep(1)
    sensor.measure()
    temperatura = sensor.temperature()
    humidade = sensor.humidity()
    print('Temperatura')
    print(temperatura)
    print('Humidade')
    print(humidade)