# -*- coding: utf-8 -*-
import socket
from threading import Thread
import sys

# Serve como um servidor para o proxy, mantém as conexões vindas dos clientes
class ClientListener:
    def __init__(self):
        self.ownIP = '127.0.0.1'
        self.ownPort = 12345
        self.serverIP = '127.0.0.1'
        self.serverPort = 12346
        self.size = 1024
        self.server = None
        self.connectedClients = []

    def create_socket(self):
        try:
            print "Criando socket..."
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.ownIP, self.ownPort))
            self.server.listen(2)
        except socket.error, (value, message):
            print "Erro de socket: " + message
            sys.exit(1)

    def start_listening(self):
        self.create_socket();

        connection, address = self.server.accept()
        newConnection = ClientConnection(connection,
                                            address,
                                            self.serverIP,
                                            self.serverPort,
                                            self.size)
        newConnection.start()
        self.connectedClients.append(c)

class ClientConnection(Thread):
    def __init__(self, connection, address, serverIP, serverPort, size):
        print "Cliente conectado: " + connection + " | endereço: " + address
        Thread.__init__(self)
        self.connection = connection
        self.address = address
        self.serverIP = serverIP
        self.serverPort = serverPort
        self.size = size

    def run(self):
        # Ips de exemplo que serão bloqueados pelo servidor por serem maliciosos

        ip_block = ['178.234.24.70','178.234.24.15','178.234.24.3']
        

        # Recebe a mensagem do cliente
        message = self.connection.recv(self.size)

        # Se recebeu
        if message:

            for ip in ip_block:
                if (message == ip):
                    negado = True
                   
            if (negado):
                msg = "Sua requisição foi negada"
                self.connection.send(msg.encode())

            else:
                # Repassa mensagem ao servidor (adicionar funcionalidade aqui)
                serverSocket = socket.socket(socket.AF_INET, SOCK_STREAM)
                serverSocket.connect((self.serverIP, self.serverPort))
                serverSocket.sendall(message)

                # Recebe resposta do servidor e repassa ao usuario
                response = serverSocket.recv(self.size)
                self.connection.sendall(self.size)

                # Se não recebeu cancela a conexão
        else:
            self.connection.close()

if __name__ == "__main__":
    s = ClientListener()
    s.start_listening()