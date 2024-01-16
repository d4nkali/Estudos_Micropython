# Teste de conectar a ESP 8266 ou ESP 32 ao WiFi

import network

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('SSID', 'Senha')
    while not sta_if.isconnected():
        pass
print('network config:', sta_if.ifconfig())
