import time
from lcd_api import LcdApi # Importa a classe base com os comandos gerais

# Esta classe herda (recebe) as funções da LcdApi e adiciona a comunicação I2C
class I2cLcd(LcdApi):
    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c           # Objeto de comunicação I2C do ESP32
        self.i2c_addr = i2c_addr # Endereço do display (geralmente 0x27)
        
        # Inicia a comunicação enviando um sinal nulo e aguarda a estabilização
        self.i2c.writeto(self.i2c_addr, bytearray([0]))
        time.sleep_ms(20)
        
        # --- Sequência de Inicialização (Protocolo HD44780) ---
        # Estes comandos resetam o controlador do LCD e o colocam em modo de 4 bits
        self.hal_write_command(0x03) 
        self.hal_write_command(0x03)
        self.hal_write_command(0x03)
        self.hal_write_command(0x02) # Define modo 4-bits para economizar pinos
        
        # Configurações de exibição:
        self.hal_write_command(0x28) # 2 linhas, matriz de caracteres 5x8
        self.hal_write_command(0x0c) # Liga o display, desliga o cursor visual
        self.hal_write_command(0x06) # Incremento automático do cursor ao escrever
        self.clear()                 # Limpa qualquer resíduo na tela

    # Método que envia COMANDOS (ex: "limpar tela", "ir para linha 2")
    def hal_write_command(self, cmd):
        # O LCD recebe os dados em duas partes (Nibbles - 4 bits cada)
        # 0x08 mantém o backlight (luz de fundo) ligado
        # 0x04 ativa o pino 'Enable' para o LCD ler o dado
        self.i2c.writeto(self.i2c_addr, bytearray([(cmd & 0xF0) | 0x08 | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytearray([(cmd & 0xF0) | 0x08]))
        self.i2c.writeto(self.i2c_addr, bytearray([((cmd << 4) & 0xF0) | 0x08 | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytearray([((cmd << 4) & 0xF0) | 0x08]))

    # Método que envia DADOS (as letras e números que aparecem na tela)
    def hal_write_data(self, data):
        # A lógica é igual ao comando, mas usa 0x09 para indicar que é um caractere
        # O bit '1' extra (0x09 em vez de 0x08) avisa ao LCD que é uma letra para exibir
        self.i2c.writeto(self.i2c_addr, bytearray([(data & 0xF0) | 0x09 | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytearray([(data & 0xF0) | 0x09]))
        self.i2c.writeto(self.i2c_addr, bytearray([((data << 4) & 0xF0) | 0x09 | 0x04]))
        self.i2c.writeto(self.i2c_addr, bytearray([((data << 4) & 0xF0) | 0x09]))