import socket
import pyaudio

# Set up server IP and port
SERVER_IP = '127.0.0.1'  # Change this to the server IP
PORT = 12345

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect the client socket to the server
    client_socket.connect((SERVER_IP, PORT))

    # Initialize PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(2),
                    channels=2,
                    rate=44100,
                    output=True)

    while True:
        # Receive audio data from the server
        data = client_socket.recv(1024)
        if not data:
            break
        stream.write(data)
except ConnectionRefusedError:
    print("Connection refused. Please make sure the server is running.")
finally:
    # Close the stream and socket
    stream.stop_stream()
    stream.close()
    client_socket.close()
