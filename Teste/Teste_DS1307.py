# Teste do Modulo RTC DS1307

# Importando as bibliotecas
from machine import I2C, Pin
import ds1307
from time import sleep

# Configurao os pinos I2C do DS1307
i2c = I2C(sda=Pin(4), scl=Pin(5))

# Inicializao o DS1307
rtc = ds1307.DS1307(i2c)

while True:
    # Ler a data e hora do RTC
    data_hora = rtc.datetime()
    # Exibe os dados da variavel data_hora
    print("Data e Hora: {}".format(data_hora))
    # Aguarda 2 segundos
    sleep(2)
