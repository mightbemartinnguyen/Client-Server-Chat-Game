import socket

gameChoices = ["rock", "paper", "scissors"]

def runClient(host='localhost', port=1121):
# Citation for the following function part1():
    # Date: 3/10/2024
    # Adapted from:
    # Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition, Pearson Chapter 2.7 Socket Programming
    # https://realpython.com/python-sockets/
    # https://docs.python.org/3.4/howto/sockets.html
    # https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
    # https://www.geeksforgeeks.org/simple-chat-room-using-python/

    # Create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        print("Welcome to the Chat Room")
        print("Type 'play game' to start a game of Rock-Paper-Scissors.")
        print("Type '/q' to quit the chat room.")
        
        while True:
            message = input("Enter Input > ").lower()
            # check for exit 
            if message == '/q':
                client.sendall(message.encode())
                print("Shutting down!")
                break
            client.sendall(message.encode())
            
            if message == "play game":
                clientChoice = input("Rock-Paper-Scissors: Type 'rock', 'paper', or 'scissors' to play > ").lower()
                print("Waiting for server's move...")
                # Validate the user's choice
                while clientChoice not in gameChoices:
                    print("Invalid choice, try again.")
                    clientChoice = input("Rock-Paper-Scissors: Type 'rock', 'paper', or 'scissors' to play > ").lower()
                # Send the user's choice to the server
                client.sendall(clientChoice.encode())
                
                # Wait for and receive the server's choice
                serverChoice = client.recv(4096).decode()
                if serverChoice not in gameChoices:
                    print("Server made an invalid choice, try again.")
                    continue
                # Wait for and receive the game result from the server
                serverResponse = client.recv(4096).decode()
                print(f"Server: {serverResponse}")
                continue

            print("Waiting for server's response...")
            # Receive data from the server
            data = client.recv(4096).decode()
            if not data:
                print("Server has closed the connection.")
                break
            print(f"Server: {data}")

if __name__ == "__main__":
    runClient()