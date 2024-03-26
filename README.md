## Integrantes

- MosquittoBroker - 0.0.0.0:1883
- ApiTest - 0.0.0.0:5000
- mqttGateway - Conectado a MosquittoBroker

- Inicio o MosquittoBroker com o comando:
	- sudo mosquitto -c mqtt.conf -v
	(-c) indica o uso do aquivo de configuração (mqtt.conf)
	(-v) Mostra logs do broker no console
	- mqtt.conf
		listener 1883 0.0.0.0
		allow_anonymous true

- Inicio a apiTest que possui as rotas:
	- http://0.0.0.0:5000/login - [POST]
		- Recebe:
		{
		"name": "Lua",
		"password": "01"
		}
		
		- Retorna:
		{
		"user": {
			"id": 1,
			"name": "Lua",
			"status": true
		},
		"access_token": "xxxxxxx"
		}		
- Ainda sem regra de negocio alguma, apenas a utilizacao da lib pydantic

- Inicio o mqttGateway:
	Ele esta inscrito (subscribe) ao topico (/topic/user/login) 
	Funcionaria da seguinte forma:
		- Quando o usuario realiza o login o codigo em JS 
		Realiza a publicação (publish) para o broker	
		no mesmo topico em que o mqttGateway esta inscrito (/topic/user/login).
		O mqttGateway então faz o request para a apiTest e retorna o resultado
		em String e transforma para JSON (!indefinido)					




