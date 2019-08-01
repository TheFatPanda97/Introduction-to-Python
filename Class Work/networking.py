import socket

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)

print("server is running...")
while True:
    c, address = s.accept()
    c.send(bytes("It is alivvvvvveeeee", 'UTF-8'))
