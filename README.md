# Client/Server Chat and Game Project

## Introduction

This project involves creating a simple client-server chat room and a multiplayer ASCII game. The client and server programs communicate over a network using socket programming and TCP.

## Project Specifications

### Writing a Client-Server Chat Program

The implementation includes two files (`server.py` and `client.py`) simulating a client-server chat on the same system. The chat works on a turn-based paradigm, where the client sends a message first, followed by the server.

**Server:**
1. Creates a socket and binds to `localhost` and a specified port.
2. Listens for a connection.
3. Receives data using `recv`.
4. Prints the data and prompts for a reply.
5. Sends the reply.
6. Repeats from step 3.
7. Closes sockets when done.

**Client:**
1. Creates a socket and connects to `localhost` and a specified port.
2. Prompts for a message to send.
3. Sends the message.
4. Receives data using `recv`.
5. Prints the data.
6. Repeats from step 2.
7. Closes sockets when done.

### Writing a Multiplayer Game

Extend the client-server chat into a multiplayer ASCII game (e.g., Tic-tac-toe, Hangman, Rock-Paper-Scissors). Players can switch from chat mode to game mode using a specific command (e.g., `play tictactoe`). After the game, the chat function resumes. Enter `/q` to quit.

## How to Run the Project

### Requirements
- Python

### Running the Server
1. Open a terminal.
2. Navigate to the directory containing `server.py`.
3. Run the server:
    ```bash
    python3 server.py
    ```

### Running the Client
1. Open another terminal.
2. Navigate to the directory containing `client.py`.
3. Run the client:
    ```bash
    python3 client.py
    ```

### Switching to Game Mode
- In the client chat, type `play [game_name]` to switch to the desired game mode.
- To exit the game or chat, type `/q`.

## Technologies Used
- Python 
- Socket programming
- TCP/IP

## Sources
- [Python Sockets Documentation](https://docs.python.org/3.4/howto/sockets.html)
- [Real Python: Python Sockets](https://realpython.com/python-sockets/)

## Authors
- Martin Nguyen

## License
This project is licensed under the MIT License.
