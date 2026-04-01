istema de Monitoramento de Temperatura com ESP32

Este projeto implementa um sistema embarcado utilizando ESP32 para monitoramento de temperatura com sensor DHT22, exibindo os dados em um display LCD via I2C e acionando um alerta visual (LED) após um tempo de estabilização.

Funcionalidades
	Leitura de temperatura em tempo real (DHT22)
	Exibição dos dados em display LCD 16x2 via I2C
	Temporizador de estabilização (20 segundos)
	Alerta visual com LED após tempo limite
	Tratamento de erros de leitura do sensor
	Atualização contínua a cada 2 segundos

Tecnologias Utilizadas
	MicroPython
	ESP32
	Sensor DHT22
	Display LCD 16x2 com módulo I2C
	GPIO (controle de LED)
	Ligações (Hardware)
	Componente	ESP32
	LCD SDA	GPIO 21
	LCD SCL	GPIO 22
	DHT22 DATA	GPIO 15
	LED	GPIO 2

O endereço I2C do LCD pode variar (geralmente 0x27)

Estrutura do Projeto
 projeto-esp32-temperatura
 ┣  boot.py        # Inicialização do sistema
 ┣  main.py        # Lógica principal
 ┣  dht.py         # Driver do sensor DHT22
 ┣  lcd_api.py     # API base do LCD
 ┣  i2c_lcd.py     # Comunicação LCD via I2C
 ┗  README.md      # Documentação

Como Funciona

O sistema inicializa o ESP32 (boot.py)
Configura:
Comunicação I2C
Display LCD
Sensor DHT22
LED de alerta
Exibe mensagem inicial: Iniciando...
Durante 20 segundos:
Mostra temperatura
Exibe contagem regressiva
Após 20 segundos:
Ativa o LED vermelho
Exibe mensagem de alerta no LCD
Execução
Instale o MicroPython no ESP32
Envie os arquivos para o dispositivo (via Thonny, ampy ou rshell)
Reinicie o ESP32

O sistema iniciará automaticamente.

	Exemplo de Saída no LCD
	Temp: 25 C
	Aguarde: 18s

Após estabilização:
		Temp: 38 C
		ALERTA: 38C +
	
	Possíveis Melhorias
	Integração com IoT (Wi-Fi / MQTT)
	Aplicativo para monitoramento remoto
	Alerta sonoro (buzzer)
	Histórico de dados (log)
	Dashboard web
	Tratamento de Erros

Caso ocorra falha no sensor:
	Mensagem exibida no LCD: Erro no Sensor
	Log no terminal para diagnóstico

Licença
Este projeto é livre para uso educacional e pessoal.

