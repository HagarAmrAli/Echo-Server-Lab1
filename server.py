import socket

# Server configuration
HOST = '127.0.0.1'  # localhost
PORT = 5000          # port number (can be changed to any number above 1024)

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))  # bind socket to IP and port
server_socket.listen(1)  # listen for one connection

print(f"Server started on {HOST}:{PORT}")
print("Waiting for client connection...")

# Accept connection from client
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Message receiving loop
while True:
    try:
        # Receive data from client
        data = conn.recv(1024).decode()
        
        # If no data received, close connection
        if not data:
            print("Client disconnected")
            break

        print(f"Received: {data}")

        # Process message based on first character
        command = data[0]  # first character of message
        text = data[1:]     # rest of message

        if command == 'A':
            # Descending order
            response = ''.join(sorted(text, reverse=True))
        elif command == 'C':
            # Ascending order
            response = ''.join(sorted(text))
        elif command == 'D':
            # Capitalize all letters
            response = text.upper()
        else:
            # Return same message
            response = data

        # Send response to client
        conn.sendall(response.encode())
        print(f"Sent: {response}\n")

    except Exception as e:
        print(f"Error: {e}")
        break

# Close connection
conn.close()
server_socket.close()
print("Server closed")