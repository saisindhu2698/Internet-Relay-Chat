# IRC Chat System

## Introduction
The **IRC (Internet Relay Chat)** system is a client-server application designed to facilitate real-time communication between multiple clients. It allows users to create rooms, join existing rooms, send messages, and leave rooms. It also supports private messaging and handles client disconnections gracefully.

---

## Features
- **Create Rooms**: Users can create their own chat rooms.
- **Join Rooms**: Clients can join available chat rooms.
- **Send Messages**: Clients can send messages to the rooms they are in.
- **Private Messages**: Clients can send messages to other clients directly.
- **Leave Rooms**: Clients can leave rooms at any time.
- **Room List**: List all available rooms to join.
- **Error Handling**: Basic error handling for invalid commands and server crashes.
- **Graceful Disconnect**: The server and clients handle disconnections smoothly.

---

## How It Works
- **Server**: The server handles multiple client connections, room management, and message distribution.
- **Client**: Clients can connect to the server, create or join rooms, and send messages to rooms or other clients.
- **Communication**: Messages between clients are sent to the server, which distributes them to the appropriate rooms.
- **Room Management**: Users can create rooms, join rooms, or leave rooms. Rooms are deleted when the last client leaves.

---

## Commands

### Client Commands:
- **`$join_room <room_name>`**: Join an existing room.
- **`$create_room <room_name>`**: Create a new room.
- **`$list_room`**: List all available rooms.
- **`$leave_room`**: Leave the current room.
- **`$exit_room`**: Disconnect from the server.
- **`$switch_room <room_name>`**: Switch to another room.

### Server Commands:
- The server automatically handles all incoming connections and message distribution based on client commands.

---

## Conclusion
This IRC system provides basic multi-client communication features with support for creating, joining, and leaving chat rooms. Future improvements could include secure messaging, encrypted communication, and additional features like file sharing and private group chats.

---
