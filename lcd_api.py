import time # Importa funções de tempo para os intervalos do hardware

class LcdApi:
    # Método construtor: define o tamanho do display (ex: 2 linhas e 16 colunas)
    def __init__(self, num_lines, num_columns):
        self.num_lines = num_lines
        self.num_columns = num_columns

    # Limpa a tela do LCD e envia o cursor para a posição inicial (0,0)
    def clear(self):
        self.hal_write_command(0x01) # Comando hexadecimal 0x01 instrui o LCD a limpar tudo
        time.sleep_ms(2) # O LCD precisa de um pequeno tempo para processar a limpeza

    # Move o cursor para uma posição específica (coluna x, linha y)
    def move_to(self, cursor_x, cursor_y):
        addr = cursor_x & 0x3f
        if cursor_y & 1: addr += 0x40 # Ajusta o endereço de memória para a linha 2
        if cursor_y & 2: addr += self.num_columns
        self.hal_write_command(0x80 | addr) # Envia o comando de posicionamento de cursor

    # Recebe uma frase (string) e escreve caractere por caractere na tela
    def putstr(self, string):
        for char in string:
            # Converte a letra em seu valor numérico (ASCII) e envia ao LCD
            self.hal_write_data(ord(char))

    # --- MÉTODOS DE ABSTRAÇÃO (HAL - Hardware Abstraction Layer) ---
    # Estes métodos abaixo "levantam um erro" propositalmente se chamados sozinhos.
    # Eles devem ser preenchidos pelo arquivo 'i2c_lcd.py' que sabe falar com o I2C.

    def hal_write_command(self, cmd):
        # Indica que este método precisa ser implementado em outra classe
        raise NotImplementedError

    def hal_write_data(self, data):
        # Indica que este método precisa ser implementado em outra classe
        raise NotImplementedError