# -*- coding: utf-8 -*-
import socket
from threading import Thread
from datetime import datetime
import sys

# cliente -> firewall -> proxy -> servidor

# Serve como um servidor para o proxy, mantém as conexões vindas dos clientes
class ClientListener:
    def __init__(self):
        self.ownIP = '127.0.0.1'
        self.ownPort = 11000
        self.serverIP = '127.0.0.1'
        self.serverPort = 11001
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

        while True:
            connection, address = self.server.accept()
            newConnection = ClientConnection(connection,
                                                address,
                                                self.serverIP,
                                                self.serverPort,
                                                self.size)
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


        # Ips de exemplo que serão bloqueados pelo servidor por serem maliciosos

        ip_block = ['178.234.24.70','178.234.24.15','178.234.24.3']

        # horas de exemplo em que o servidor não pode ser acessado

        horas_proibidas = ['21', '23', '12']

        clientes_conectados = {}

        clientes_bloqueados = {}




        while True:

            now = datetime.now()

            # Recebe a mensagem do cliente
            message = self.connection.recv(self.size)

            clientIp = self.address[0]

            hora_conexao = str(now).split(" ")[1]



            clientes_conectados[self.address[0]] = []
            clientes_conectados[self.address[0]].append(hora_conexao)

            # Se recebeu
            if message:
                negado = False
                for ip in ip_block:
                    if (clientIp == ip):
                        negado = True
                       
                if (negado):
                    msg = "Sua requisição foi negada"
                    self.connection.send(msg.encode())
                    self.connection.close()

                else:

                    hora = int(elemento.split(':')[0])
                    
                    for h in horas_proibidas:
                        if ( hora == h):
                            msg = "Sua requisição foi negada"
                            self.connection.send(msg.encode())
                            self.connection.close()



                    for item in clientes_conectados:

                        horas = []
                        minutos = []
                        segundos[]

                        for elemento in clientes_conectados[item]:

                            hora = int(elemento.split(':')[0])
                            minuto = int(elemento.split(':')[1])
                            segundo = int(elemento.split(':')[2])

                            horas.append(hora)
                            minutos.append(minuto)
                            segundos.append(segundo)

                        
                        cont = 0; 
                        for i in xrange(1,10):
                            
                            if((horas[i] == horas[i+1]) and (minutos[i] == minutos[i+1]) and ((i+1) <= 10)):
                                cont++
                        
                        if (cont == 10):
                            clientes_bloqueados[item] = str(now).split(" ")[1]
                            msg = "Sua requisição foi negada"
                            self.connection.send(msg.encode())
                            self.connection.close()   
                             
                        else: 
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