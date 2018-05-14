import socket

# cliente -> firewall -> proxy -> servidor

HOST = '127.0.0.1'     # Server IP
PORT = 11000           # Server port
SIZE = 1024			   # Buffer sizer

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
s.connect(dest)

print 'Connecting...\n'
msg = raw_input('Write your message: ')

if msg:
    s.sendall(b'Message: {}'.format(msg))
    print 'Send message\n'

    response = s.recv(SIZE)
    print 'Response: '+response;

print 'Closing connection...'
s.close()