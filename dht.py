import array        # Importa o módulo para manipular arrays de bytes (economiza memória)
import micropython  # Importa funções específicas do ecossistema MicroPython
import utime        # Importa funções de tempo (delay e contagem)
from machine import Pin # Importa o controle dos pinos GPIO do ESP32

# Classe base que define o comportamento genérico para sensores da família DHT
class DHTBase:
    def __init__(self, pin):
        self.pin = pin  # Armazena o pino onde o sensor está conectado
        # Configura o pino como Entrada (IN) e ativa o resistor interno de Pull-up
        self.pin.init(Pin.IN, Pin.PULL_UP)
        # Cria um buffer (espaço na memória) de 5 bytes para armazenar os dados do sensor
        self.buf = array.array("B", [0]*5)

    def measure(self):
        # Este método seria responsável por ler os pulsos elétricos do sensor real.
        # No simulador Wokwi, a lógica complexa de tempo é tratada internamente.
        pass

    def temperature(self):
        # Retorna o valor da temperatura. No Wokwi, este valor fixo (25.0) 
        # é interceptado e substituído pela posição do slider no simulador.
        return 25.0 

# Classe específica para o DHT22 que herda as características da classe base
class DHT22(DHTBase):
    pass