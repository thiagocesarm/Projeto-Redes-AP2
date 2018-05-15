import socket
import json

# cliente -> firewall -> proxy -> servidor

HOST = '127.0.0.1'     # Server IP
PORT = 11000           # Server port
SIZE = 1024			   # Buffer size

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
s.connect(dest)

print('Connecting...\n')

while True:
	msg = raw_input('Choose the functionality: \n Write "time" to get the time of the moment \n Write "server-visits" to get the number of visitors \n Write "http" to make an http request \n\n Write "close" to close connection \n\n')
	body = ''
	
	if msg != 'close':
	    if msg == 'http':
	    	body = raw_input('\nYou have chosen the http request option, enter the request address: \n')

	    req = '{"type": "request", "service": "'+msg+'", "body": "'+body+'"}'
	    s.sendall(req)
	    print('\nMessage sent')

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