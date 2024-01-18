# Teste do sensor de pressão atmosferica BMP180

# Importa as bibliotecas
from machine import I2C, Pin
from time import sleep
import bmp180

# Configuração dos pinos I2C do BMP180
i2c = I2C(sda=Pin(4), scl=Pin(5))

# Inicializa o BMP180
bmp = bmp180.BMP180(i2c)

while True:
    # Cria a variavel pressao e armazena os dados do sensor
    pressao = bmp.pressure
    # Imprime os dados
    print("Pressão: {}hPa".format(pressao))
    # Aguarda 2 segundos
    sleep(2)
