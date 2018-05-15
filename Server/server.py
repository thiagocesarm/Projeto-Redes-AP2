import socket

HOST = '127.0.0.1'              # Server IP
PORT = 11002     		        # Server Port
SIZE = 1024            			# Buffer size

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

print 'Server running on port ', PORT, '\n'

while True:
    con, client = tcp.accept()
    print 'Connection established with ', client

    while True:
        msg = con.recv(SIZE)
        if not msg: break
        print client, msg
        con.send('{"type" : "response", "service" : "test", "body" : "test"}')

    print 'Closing connection with client ', client
    con.close()
