import socket

sock = socket.socket()
sock.connect(('localhost', 8888))
# sock.send('hello, world!')

data = sock.recv(1024)
sock.close()

print(data)
