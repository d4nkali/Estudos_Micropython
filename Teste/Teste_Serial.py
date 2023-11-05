import machine
import time

# Cria a variavel  para a porta analógica A0
pin_ldr = machine.ADC(0)

# Inicia a comunicação com o monitor serial
import serial
monitor = serial.Serial(0)  # 0 é o número da porta serial padrão no ESP8266

while True:

    # Lê o valor do LDR
    valor_ldr = pin_ldr.read()

    # Exibe o valor no monitor serial
    print("Valor do LDR:", valor_ldr)

    # Aguarda 1 segundo
    time.sleep(1)
