import socket


class LiftClient:

    def send_command(self, command: str) -> bool:
        HOST, PORT = "localhost", 9999
        # Create a socket (SOCK_STREAM means a TCP socket)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server and send data
        try:
            sock.connect((HOST, PORT))
            sock.sendall(bytes(command + "\n", "utf-8"))
            print("Sent:     {}".format(command))
            # Receive data from the server and shut down
            received = str(sock.recv(1024), "utf-8")
            print("Received: {}".format(received))
            return True
        except ConnectionRefusedError:
            return False
