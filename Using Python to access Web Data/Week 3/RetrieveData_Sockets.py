#Code Author: José Carlos del Castillo Estrada

#Excercise solved from the book "Python for Everybody" by Dr. Charles R. Severance
#Following the Coursera program "Using Python to access Web Data" by the University of Michigan

'''
Retrieve data with the HTTP protocol using sockets and print it
'''

import socket
#This makes the connection
mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect( ('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mySock.send(cmd)

while True:
    #The number is = to the # of chars to recieve 
    data = mySock.recv(612)
    if (len(data) < 1):
        break
    print(data.decode())
mySock.close()