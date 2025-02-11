#edited
import threading
import socket
import sys

username = input("Enter Your Name: ")
threads = []

# stating the connection
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 64526))

#communicating with server by sending and receiving messages
def sendMessages():
    while True:
        userMessage = '{} {}'.format(username, input(''))
        try:
            client.send(userMessage.encode('utf-8'))
        except:
            sys.exit(0)

def receiveMessages():
    while True:
        try:
            userMessage = client.recv(1024).decode('utf-8')
            if userMessage == 'U_NAME':
                client.send(username.encode('utf-8'))
            elif userMessage == 'EXIT':
                sys.exit(2)
            else:
                print(userMessage)
        except Exception as e:
            print('SERVER NOT RESPONDING')
            client.close()
            sys.exit(2)

receive_thread = threading.Thread(target=receiveMessages)
receive_thread.start()
threads.append(receive_thread)
send_thread = threading.Thread(target=sendMessages)
send_thread.start()
threads.append(send_thread)