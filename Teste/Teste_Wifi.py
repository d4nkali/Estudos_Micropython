# Teste de conectar a ESP 8266 ou ESP 32 ao WiFi

# Importa a biblioteca
import network

ssid = 'Seu_wifi' # Substituir a variavel SSID pelo nome do wifi da sua preferencia
senha = 'Senha_do_seu_wifi' # Substituir a variavel Senha para a senha do wifi da sua preferencia
sta_if = network.WLAN(network.STA_IF) # Cria uma variavel de configurao da biblioteca

if not sta_if.isconnected(): # Se o wifi no conectar, ento:
    print('Conectando ao WiFi...') # Imprime a mensagen de conectar a rede
    sta_if.active(True) # Ativa o wifi
    sta_if.connect(ssid, senha) # Conecta ao wifi 
    while not sta_if.isconnected(): # Se no conectar
        pass # Cria o loop at conectar a rede
print('Informaes da Rede: ', sta_if.ifconfig()) # Imprime as informaes da rede
