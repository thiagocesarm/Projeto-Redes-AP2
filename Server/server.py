import socket

HOST = ''              # Server IP
PORT = 12345           # Server Port
SIZE = 1024            # Buffer size

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

print 'Server running on port ' + PORT + '\n'

while True:
    con, client = tcp.accept()
    print 'Connection established with ', cliente

    while True:
        msg = con.recv(SIZE)
        if not msg: break
        print client, msg
        con.send('Message received!')

    print 'Closing connection with client ', client
    con.close()