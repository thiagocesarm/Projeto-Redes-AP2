import socket
import sys

class Socket:

    def __init__(self):
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conexao(self, ip, port=1911):
        self.sock.connect((ip, port))

    def esperandoConexao(self, ip='', port=1911, l=1):
        self.sock.bind((ip, port))
        self.sock.listen(l) 
        (clientsocket, address) = self.sock.accept()
        self.sock = clientsocket 
    
    def enviar(self, msg):
        sent = self.sock.send(msg)
        if sent == 0:
            raise BrokenCon, "socket connection broken"

    def receber(self, bytes):
        return self.sock.recv(bytes)

    def fechar(self):
        self.sock.close()


   
def enviaDecisao(skt, pwd):


def recebendoRequisicao(skt, pwd):      


def Firewall():
    

if __name__ == '__main__':
    Firewall()