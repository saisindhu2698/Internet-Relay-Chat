import socket
import threading

host = '127.0.0.1'
#(port can be less than 65535)
port = 64526  

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

steps = '\nApplication Menu:\n' \
               '1.menu\n' \
               '2.create room\n' \
               '3.join room\n' \
               '4.switch room\n' \
               '5.leave room\n' \
	       '6.list room\n' \
               '7.personal message\n' \
               '8.exit room\n'

roomEntries = {}
users = {}
usersOfRoom = {}
clients = []
userNames = []

# start braodcasting of messages
def broadcastMessage(userMessage, roomName):
    for client in roomEntries[roomName].peoples:
        userInput = '['+roomName+'] '+userMessage
        client.send(userInput.encode('utf-8'))
