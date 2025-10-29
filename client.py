import socket

# Connection configuration (must match server settings)
HOST = '127.0.0.1'  # localhost
PORT = 5000          # same port as server

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
try:
    client_socket.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}")
    print("\nInstructions:")
    print("  Start with 'A' for descending sort (e.g., Ahello)")
    print("  Start with 'C' for ascending sort (e.g., Cworld)")
    print("  Start with 'D' for capitalization (e.g., Dpython)")
    print("  Type 'exit' to quit\n")

    # Message sending and receiving loop
    while True:
        # Get message from user
        msg = input("Enter message: ")
        
        # If user types exit, close connection
        if msg.lower() == 'exit':
            print("Closing connection...")
            break

        # Send message to server
        client_socket.sendall(msg.encode())
        
        # Receive response from server
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}\n")

except ConnectionRefusedError:
    print("Could not connect to server. Make sure the server is running!")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Close socket
    client_socket.close()
    print("Client closed")