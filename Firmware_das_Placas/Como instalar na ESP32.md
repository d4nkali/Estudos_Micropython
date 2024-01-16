# Como Instalar o MicroPython

1) Baixe o **MicroPython**:

Acesse o site oficial do [MicroPython nesse link](https://micropython.org/) e vá para a seção de **downloads**. Escolha a versão adequada para a sua placa ESP32. Faça o download do firmware apropriado para o seu dispositivo.

#

2) Instale o **Python** (caso não tenha):

O **MicroPython** é uma implementação mínima do **Python** e requer o Python instalado no seu computador. Você pode baixar a versão mais recente do [Python para Windows](https://www.python.org/downloads/windows/) ou do [Python para Linux](https://python.org.br/instalacao-linux/).

#

3) Instale as ferramentas necessárias:

Você precisará das ferramentas para gravar o firmware na placa. Para **ESP32** o `esptool.py`.

Para instalar o `esptool.py` no Windows, abra o prompt de comando (cmd) e no Linux, abra o seu terminal e execute o seguinte comando (você pode precisar usar *pip3* em vez de pip dependendo da sua configuração):


`pip install esptool.py` ou `pip install esptool`

#

4) Limpe a placa:

Antes de instalar o MicroPython, certifique de que a sua **ESP32** esteja sem codigo, para isso no Windows execute o seguinte codigo para **ESP32** (substitua x pela porta onde esta conectada a placa):

`esptool --port COMx erase_flash`

No linux:

`esptool.py --port /dev/ttyUSBx erase_flash` 

#

5) Grave o MicroPython na placa:

Conecte a placa ao seu computador via USB e abra o prompt de comando ou terminal.

Para **ESP32**, use o seguinte comando (substitua `COMx` e `"esp32-firmware".bin` conforme necessário):

`esptool.py --chip esp32 --port COMx --baud 115200 write_flash -z 0x1000 "esp32-firmware".bin`

No terminal do Linux:

`esptool.py --chip esp32 --port /dev/ttyUSBx --baud 115200 write_flash -z 0x1000 "esp32-firmware".bin`

#

6) Instale uma IDE :

Após gravar o **MicroPython** na placa, baixe uma IDE com suporte ao MicroPython como a [Arduino Labs](https://labs.arduino.cc/en/labs/micropython) ; apos instalar abra o programa e em conect e selecione a porta da placa.

#

Agora você deve ter o MicroPython instalado e funcionando na sua placa **ESP32** no Windows ou Linux. Você pode começar a programar em Python na placa e aproveitar todas as funcionalidades do MicroPython.