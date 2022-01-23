import socket
import sys

if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 9999
    isExit = False

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server
        sock.connect((HOST, PORT))
        while True:
            data = ""
            try:
                data = sys.stdin.readline()

                sock.sendall(bytes(data + "\n", "utf-8"))
                received = str(sock.recv(1024), "utf-8")

                print("Sent:     {}".format(data))
                print("Received: {}".format(received))
            except KeyboardInterrupt:
                break
