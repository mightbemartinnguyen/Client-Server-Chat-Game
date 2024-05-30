import socket

gameChoices = ["rock", "paper", "scissors"]

def rockPaperScissors(serverChoice, clientChoice):
    if serverChoice == clientChoice:
        return "It's a tie!"
    elif (serverChoice == "rock" and clientChoice == "scissors") or \
         (serverChoice == "scissors" and clientChoice == "paper") or \
         (serverChoice == "paper" and clientChoice == "rock"):
        return "Server wins!"
    else:
        return "Client wins!"

def runServer(port=1121):
# Citation for the following function part1():
    # Date: 3/10/2024
    # Adapted from:
    # Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition, Pearson Chapter 2.7 Socket Programming
    # https://realpython.com/python-sockets/
    # https://docs.python.org/3.4/howto/sockets.html
    # https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
    # https://www.geeksforgeeks.org/simple-chat-room-using-python/

    # create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('localhost', port))
        server.listen()
        print(f"Server listening on: localhost on port: {port}")

        clientSocket, clientAddress = server.accept()
        with clientSocket:
            print(f"Connected by {clientAddress}")
            # loop to recieve data
            while True:
                print("Waiting for message...")
                data = clientSocket.recv(4096).decode().lower()
                if not data or data == '/q':
                    print("Client has requested shutdown. Shutting down!")
                    break
                # Check if the client wants to play the game
                if data == "play game":
                    print("Waiting for the client's move...")
                    clientChoice = clientSocket.recv(4096).decode().lower()
                    # Validate the client's choice
                    if clientChoice not in gameChoices:
                        clientSocket.sendall("Invalid choice.".encode())
                        continue
                    
                     # Prompt the server user for their choice
                    serverChoice = input("Enter rock, paper, or scissors > ").lower()
                    # Validate the server's choice
                    while serverChoice not in gameChoices:
                        print("Invalid choice, choose again.")
                        serverChoice = input("Enter rock, paper, or scissors > ").lower()

                    clientSocket.sendall(serverChoice.encode())  # Send server's choice

                    # Determine and send the game result
                    result = rockPaperScissors(serverChoice, clientChoice)
                    clientSocket.sendall(f"{result} Server chose {serverChoice}. Client chose {clientChoice}.".encode())
                    continue
                
                # If not playing a game, proceed with the chat functionality
                print(f"Client: {data}")
                reply = input("Enter Input > ")
                if reply.lower() == '/q':
                    clientSocket.sendall(reply.encode())
                    break
                # Send the reply to the client
                clientSocket.sendall(reply.encode())

if __name__ == "__main__":
    runServer()