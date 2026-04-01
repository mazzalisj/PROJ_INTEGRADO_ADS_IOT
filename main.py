import machine          # Acesso aos recursos de hardware do ESP32
import dht              # Biblioteca para comunicação com o sensor DHT22
import time             # Controle de temporização e pausas
from machine import I2C, Pin
from i2c_lcd import I2cLcd # Importa o driver para controlar o display via I2C

# 1. Configuração da Comunicação I2C e Display LCD
# Define os pinos 22 (SCL) e 21 (SDA) para o display, com frequência de 400kHz
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
# Inicializa o LCD no endereço 0x27, com 2 linhas e 16 colunas
lcd = I2cLcd(i2c, 0x27, 2, 16)

# 2. Configurações de Sensores e Atuadores
# Configura o sensor de temperatura no pino 15
sensor = dht.DHT22(Pin(15))
# Configura o LED de alerta no pino 2 como uma saída de sinal
led_alerta = Pin(2, Pin.OUT)

# Variável acumuladora para controlar o tempo de estabilização do sistema
tempo_decorrido = 0

# Mensagem inicial ao ligar o aparelho
lcd.putstr("Iniciando...")
time.sleep(2) # Pausa necessária para o sensor estabilizar

while True:
    try:
        # Solicita uma nova leitura dos dados do sensor
        sensor.measure()
        temp = sensor.temperature()
        
        # Incrementa o contador (o loop roda a cada 2 segundos devido ao sleep no fim)
        tempo_decorrido += 2
        
        # Atualiza a interface visual do utilizador
        lcd.clear() # Limpa a tela para evitar sobreposição de caracteres
        lcd.putstr("Temp: {} C".format(temp)) # Exibe temperatura na primeira linha
        
        # 3. Lógica de Segurança e Alerta (Janela de 20 segundos)
        if tempo_decorrido >= 20:
            # Após o tempo de aquecimento/estabilização, o alerta é ativado
            led_alerta.value(1)         # Liga o LED de aviso
            lcd.move_to(0, 1)           # Posiciona o cursor na segunda linha
            lcd.putstr("ALERTA: 38C +") # Exibe aviso crítico no visor
            print("!!! ALERTA DE SEGURANÇA: 20s atingidos - Agua Quente !!!")
        else:
            # Durante a fase inicial de 20 segundos, o sistema apenas monitoriza
            led_alerta.value(0)         # Garante que o LED está desligado
            lcd.move_to(0, 1)           # Move para a segunda linha
            # Mostra ao utilizador quanto tempo falta para o sistema estar pronto
            lcd.putstr("Aguarde: {}s".format(20 - tempo_decorrido))
            
        # Pausa obrigatória de 2 segundos (tempo mínimo de resposta do sensor DHT22)
        time.sleep(2)
        
    except OSError:
        # Caso haja falha na fiação ou mau contato com o sensor
        lcd.clear()
        lcd.putstr("Erro no Sensor")
        print("Erro de leitura: Verifique as conexões do DHT22")