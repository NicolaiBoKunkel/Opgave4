#Klient Opgave 4

from socket import *

servername = "localhost"
serverport = 10

clientsocket = socket(AF_INET, SOCK_STREAM)
clientsocket.connect((servername, serverport))

operation = input("indtast funktion (Add, Random eller Subtract):")
num1 = input('Indtast tal 1:')
num2 = input('Indtast tal 2:')
data = (operation+';'+num1+';'+num2).encode()
clientsocket.send(data)

datatilbage = clientsocket.recv(2048)
sentanceTilbage = datatilbage.decode()

print ("modtaget resultat:", sentanceTilbage)

clientsocket.close