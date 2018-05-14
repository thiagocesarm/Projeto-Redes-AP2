# -*- coding: utf-8 -*-
import socket
from threading import Thread
import sys

# Serve como um servidor para o proxy, mantém as conexões vindas dos clientes
class ClientListener:
	def __init__(self):
		self.ownIP = '127.0.0.1'
		self.ownPort = 11001
		self.serverIP = '127.0.0.1'
		self.serverPort = 11002
		self.size = 1024
		self.server = None
		self.connectedClients = []
		self.listen = 10

	def create_socket(self):
		try:
			print "Criando socket..."
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server.bind((self.ownIP, self.ownPort))
			self.server.listen(self.listen)
		except socket.error, (value, message):
			print "Erro de socket: " + message
			sys.exit(1)

	def start_listening(self):
		self.create_socket();

		while True:
			connection, address = self.server.accept()
			newConnection = ClientConnection(connection, address, self.serverIP, self.serverPort, self.size)
			newConnection.start()
			self.connectedClients.append(newConnection)

class ClientConnection(Thread):
	def __init__(self, connection, address, serverIP, serverPort, size):
		print "Cliente conectado: ", connection, " | endereço: ", address
		Thread.__init__(self)
		self.connection = connection
		self.address = address
		self.serverIP = serverIP
		self.serverPort = serverPort
		self.size = size

	def run(self):
		# Loop infinito até o cliente desconectar
		while True:
			# Recebe a mensagem do cliente
			message = self.connection.recv(self.size)

			# Se recebeu
			if message:
				# Repassa mensagem ao servidor (adicionar funcionalidade aqui)
				serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				serverSocket.connect((self.serverIP, self.serverPort))
				serverSocket.sendall(message)

				# Recebe resposta do servidor e repassa ao usuario
				response = serverSocket.recv(self.size)
				self.connection.sendall(response)

			# Se não recebeu cancela a conexão
			else:
				self.connection.close()
				break

if __name__ == "__main__":
	s = ClientListener()
	s.start_listening()