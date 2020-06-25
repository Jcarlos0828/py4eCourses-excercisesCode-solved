import socket
#This makes the connection
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect( ('domain.com', 80))
cmd = 'GET URL HTTP/1.0\r\n\r\n'.encode()
mySock.send(cmd)

while True:
    data = mySock.recv(612)
    if (len(data) < 1):
        break
    print(data.decode())
mySock.close()