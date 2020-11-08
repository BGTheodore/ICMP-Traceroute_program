import socket

host = '127.0.0.1'  
port = 6332        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    sock.sendall(b'Hello, world')
    donnee = sock.recv(1024)

print('Recu', repr(donnee))