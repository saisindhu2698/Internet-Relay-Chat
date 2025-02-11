from main import *

class User:
    def __init__(self, name):
        self.name = name
        self.roomEntries = []
        self.thisRoom = ''


class Room:
    def __init__(self, name):
        self.peoples = []
        self.userNames = []
        self.name = name

#Retrieve available rooms list.
def roomDetailsList(inputname):
    name = users[inputname]
    print(len(roomEntries))
    if len(roomEntries) == 0:
        name.send('There are no rooms left; you cannot join\n'.encode('utf-8'))
    else:
        reply = "The List of available rooms and members are: \n"
        name.send(f'{reply}'.encode('utf-8'))
        for room in roomEntries:
            print(roomEntries[room].name)
            print(roomEntries[room].userNames)
            name.send(f'{roomEntries[room].name}\n'.encode('utf-8'))
            name.send(f'{roomEntries[room].userNames}\n'.encode('utf-8'))


#Creating new rooms
def CreateNewRoom(inputname, newroomname):
    name = users[inputname]
    user = usersOfRoom[inputname]
    if not newroomname:
        name.send('Enter the Name of room to Create!, Your entry dont contain room Name\n'.encode('utf-8'))
    elif newroomname not in roomEntries:
        room = Room(newroomname)
        roomEntries[newroomname] = room
        room.peoples.append(name)
        room.userNames.append(inputname)
        user.thisRoom = newroomname
        user.roomEntries.append(room)
        name.send(f'{newroomname} created\n'.encode('utf-8'))
    else:
        if newroomname in user.roomEntries:
            name.send('Please enter a different name for the room, there is already a room with that name.\n'.encode('utf-8'))


#Joining rooms
def joinNewRoom(inputname, newroomname):
    name = users[inputname]
    user = usersOfRoom[inputname]
    print(len(roomEntries))
    if len(roomEntries) == 0:
        name.send('At present No rooms are available to join\n'.encode('utf-8'))
    else:
        room = roomEntries[newroomname]
        if newroomname in user.roomEntries:
            name.send('You are existing member of the room\n'.encode('utf-8'))
        else:
            room.peoples.append(name)
            room.userNames.append(inputname)
            user.thisRoom = newroomname
            user.roomEntries.append(room)
            broadcastMessage(f'{inputname} joined the room', newroomname)
            broadcastMessage(f'{inputname} Welcome to the room', newroomname)


#switch to another room.
def switchNewRoom(inputname, roomName):
    user = usersOfRoom[inputname]
    name = users[inputname]
    room = roomEntries[roomName]
    if roomName == user.thisRoom:
        name.send('You are already a member of the room; select an alternative room to switch.\n'.encode('utf-8'))
    elif room not in user.roomEntries:
        name.send('You cannot change rooms because you are not a part of the room.\n'.encode('utf-8'))
    else:
        user.thisRoom = roomName
        name.send(f'You are successfully switched to {roomName}\n'.encode('utf-8'))


#Leave Room Functionality
def leaveRoomFunc(inputname):
    user = usersOfRoom[inputname]
    name = users[inputname]
    if user.thisRoom == '':
        name.send('You are not a member of any room\n'.encode('utf-8'))
    else:
        roomName = user.thisRoom
        room = roomEntries[roomName]
        user.thisRoom = ''
        user.roomEntries.remove(room)
        roomEntries[roomName].peoples.remove(name)
        roomEntries[roomName].userNames.remove(inputname)
        broadcastMessage(f'{inputname} left the room!\n', roomName)
        name.send('You left the room!\n'.encode('utf-8'))


#Transfer Personal Messages
def personalMsgTransfer(userMessage):
    args = userMessage.split(" ")
    user = args[2]
    sender = users[args[0]]
    sender.send('You can start sending messages'.encode('utf-8'))
    if user not in users:
        sender.send('User not found\n'.encode('utf-8'))
    else:
        recieverVar = users[user]
        clientMsg = ' '.join(args[3:])
        recieverVar.send(f'[personal message] {args[0]}: {clientMsg}'.encode('utf-8'))
        sender.send(f'[personal message] {args[0]}: {clientMsg}'.encode('utf-8'))

        

#Exit of server/application
def removeClientFunc(inputname):
    userNames.remove(inputname)
    client = users[inputname]
    user = usersOfRoom[inputname]
    user.thisRoom = ''
    for room in user.roomEntries:
        print(room.name)
        room.peoples.remove(client)
        print(room.peoples)
        room.userNames.remove(inputname)
        print(room.userNames)
        broadcastMessage(f'{inputname} left the room\n', room.name)


#handle
def handle(client):
    nameOfUser=''
    while True:
        try:
            userMessage = client.recv(1024).decode('utf-8')
            args = userMessage.split(" ")
            name = users[args[0]]
            nameOfUser = args[0]
            if 'menu' in userMessage:
                name.send(steps.encode('utf-8'))
            elif 'list' in userMessage:
                roomDetailsList(args[0])
            elif 'create' in userMessage:
                CreateNewRoom(args[0], ' '.join(args[2:]))
            elif 'join' in userMessage:
                joinNewRoom(args[0], ' '.join(args[2:]))
            elif 'leave' in userMessage:
                leaveRoomFunc(args[0])
            elif 'switch' in userMessage:
                switchNewRoom(args[0], args[2])
            elif 'personal' in userMessage:
                personalMsgTransfer(userMessage)
            elif 'exit' in userMessage:
                removeClientFunc(args[0])
                name.send('EXIT'.encode('utf-8'))
                name.close()
            else:
                if usersOfRoom[args[0]].thisRoom == '':
                    name.send('You are not member of any room\n'.encode('utf-8'))
                else:
                    clientMsg = ' '.join(args[1:])
                    broadcastMessage(f'{args[0]}: {clientMsg}',usersOfRoom[args[0]].thisRoom)

        except Exception as e:
            print("exception occured ", e)
            index = clients.index(client)
            clients.remove(client)
            client.close()
            print(f'User Name is {nameOfUser}')
            if nameOfUser in userNames:
                removeClientFunc(nameOfUser)
            if nameOfUser in userNames:
                userNames.remove(nameOfUser)
            break

#main
def receiveClientMessages():
    while True:
        client, address = server.accept()
        print(f'Got connection with {str(address)}\n')
        print(client)
        client.send('U_NAME'.encode('utf-8'))
        inputname = client.recv(1024).decode('utf-8')
        userNames.append(inputname)
        clients.append(client)
        user = User(inputname)
        usersOfRoom[inputname] = user
        users[inputname] = client
        print(f'Name of the client is {inputname}\n')
        client.send('\nConnected to the server!!\n'.encode('utf-8'))
        client.send(steps.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
print('Connection established')
print('Server Started')
receiveClientMessages()