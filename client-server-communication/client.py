import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 9000))

command = "GET http://127.0.0.1/romeo.txt HTTP/1.1\r\n\r\n".encode()
my_socket.send(command)

while True:
    data = my_socket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

my_socket.close()
