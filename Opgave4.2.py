#Server Opgave 4

from socket import *
import threading
import random

def handleOneClient(connectionSocket, address):
    print('Address', address)

    data = connectionSocket.recv(2048).decode()
    parts = data.split(';')

    if len(parts) == 3:
        operation = parts[0]
        num1 = int(parts[1])
        num2 = int(parts[2])

        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Random':
            result = random.randint(num1, num2)
        else:
            result = 'Invalid input'

        response = f'Resultat;{result}'
        connectionSocket.send(response.encode())
    else:
        connectionSocket.send('Invalid input'.encode())

    connectionSocket.close()

serverPort = 10

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to work for you')

while True:
    clientSocket, clientAddress = serverSocket.accept()
    threading.Thread(target=handleOneClient, args=(clientSocket, clientAddress)).start()
