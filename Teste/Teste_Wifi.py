# Teste de conectar a ESP 8266 ou ESP 32 ao WiFi

# Importa a biblioteca
import network

sta_if = network.WLAN(network.STA_IF) # Cria uma variavel de configurao da biblioteca

if not sta_if.isconnected(): # Se o wifi no conectar, ento:
    print('connecting to network...') # Imprime a mensagen de conectar a rede
    sta_if.active(True) # Ativa o wifi
    sta_if.connect('SSID', 'Senha') # Conecta ao wifi onde substituir o SSID pelo nome do wifi e a senha para o wifi da sua preferencia
    while not sta_if.isconnected(): # Se no conectar
        pass # Cria o loop at conectar a rede
print('network config:', sta_if.ifconfig()) # Imprime as informaes da rede
