import socket

host = '127.0.0.1'  # Adresse du serveur local alias localhost
port = 6332        # Port exige

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: #AF_INET pour preciser la famille d’adresse, dans ce cas IPV4 et SOCK_STREAM pour forcer TCP
    sock.bind((host, port))
    sock.listen()
    connection, adresse = sock.accept()
    with connection:
        print('Connecte par', adresse)
        while True:
            donnee = connection.recv(1024)
            if not donnee:
                break
            connection.sendall(donnee)