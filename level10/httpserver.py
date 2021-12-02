import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ("ip", 6969)
server.bind(addr)
server.listen(5)
print("addr = %s, port = %s" % addr)
while True:
    print("En attente...")
    (client, adressClient) = server.accept()
    print('Connexion de ', adressClient)
    while True:
        data = client.recv(1024)
        print('recu: "%s"' % data)
        if len(data) < 1:
            client.close()
            break
    break


