# Ficheiro boot.py - Este é o primeiro ficheiro que o ESP32 executa ao ligar
import gc   # Importa o 'Garbage Collector' para gestão inteligente de memória
import esp  # Importa funções específicas do sistema do microcontrolador ESP32

# Desativa mensagens de debug (erros de baixo nível) do sistema operativo do ESP32
# Isso evita que o terminal fique "poluído" com textos técnicos antes do seu programa [cite: 31]
esp.osdebug(None)

# Executa a limpeza da memória RAM. É uma boa prática para garantir que o 
# programa principal (main.py) tenha o máximo de espaço disponível para rodar 
gc.collect()

# Exibe uma mensagem de confirmação no Serial Monitor indicando que a fase de boot terminou
print("Boot concluído com sucesso. A iniciar o sistema do lavatório...")