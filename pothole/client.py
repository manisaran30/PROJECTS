import socket
import time

# Client configuration
server_ip = "127.0.0.1"
server_port = 12345

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Simulate pothole detection (replace this with actual pothole detection logic)
    pothole_data = "Pothole detected at GPS coordinates: (X, Y)"

    # Send the pothole warning to the server
    client_socket.sendto(pothole_data.encode('utf-8'), (server_ip, server_port))

    print(f"Pothole warning sent to {server_ip}:{server_port}")

    # Add a delay before sending the next warning (replace this with your desired interval)
    time.sleep(5)
