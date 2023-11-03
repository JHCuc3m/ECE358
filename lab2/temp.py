from socket import *

serverIP = "127.0.0.1"  # local host address
serverPort = 12000  # anything 1023 or above
serverSocket = socket(AF_INET, SOCK_STREAM)  # create TCP welcoming socket
serverSocket.bind((serverIP, serverPort))  # bind the socket to the port
serverSocket.listen(1)  # server begins listening for incoming TCP requests
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()  # server waits on accept() for incoming requests, new socket created on return
    sentence = connectionSocket.recv(2048).decode()  # read bytes from socket (but not address as in UDP)
    capitalizedSentence = sentence.upper()  # change sentence to upper case
    connectionSocket.send(capitalizedSentence.encode())  # send back modified sentence
    connectionSocket.close()  # close connection to this client (but not welcoming socket)
