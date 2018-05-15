# -*- coding: utf-8 -*-
import socket
import json

# cliente -> firewall -> proxy -> servidor

HOST = '127.0.0.1'     # Server IP
PORT = 11001           # Server port
SIZE = 1024			   # Buffer size

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
s.connect(dest)

print('Connecting...\n')

# Enquanto o usuário não escolher a opção de fechar a conexão
while True:
	# Recebe o funcionalidade a ser executada 
	msg = raw_input('Choose the functionality: \n Write "time" to get the time of the moment \n Write "server-visits" to get the number of visitors \n Write "http" to make an http request \n\n Write "close" to close connection \n\n')
	body = ''
	
	# Se não for escolhido a opção de fechar conexão
	if msg != 'close':
		# Se o serviço for o de requisição http
	    if msg == 'http':
	    	# Recebe o endereço do servidor no qual a irá ser feito a requisição http
	    	body = raw_input('\nYou have chosen the http request option, enter the request address: \n')

	    # Envia mensagem em JSON 
	    req = '{"type": "request", "service": "'+msg+'", "body": "'+body+'"}'
	    s.sendall(req)
	    print('\nMessage sent')

	    # Recebe e decodifica a mensagem em JSON  do servidor
	    response = json.loads(s.recv(SIZE))
	    print('Response: '+response['body']+' \n')

	    resp = raw_input('Continue? (y/n): ')
	    
	    if resp == 'n':
	    	print('Closing connection...')
	    	break

	else:
		print('Closing connection...')
		break

s.close()