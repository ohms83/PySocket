import socket
import sys

HOST, PORT = '127.0.0.1', 9999

if len(sys.argv) >= 2:
    HOST = sys.argv[1]
if len(sys.argv) >= 3:
    PORT = sys.argv[2]

# SOCK_DGRAM is the socket type to use for UDP sockets
print("Connecting to server at {0} port: {1}".format(HOST, PORT))
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    while True:
        data = ""
        try:
            data = sys.stdin.readline()

            # As you can see, there is no connect() call; UDP has no connections.
            # Instead, data is directly sent to the recipient via sendto().
            sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
            received = str(sock.recv(1024), "utf-8")

            print("Sent:     {}".format(data))
            print("Received: {}".format(received))
        except KeyboardInterrupt:
            break
