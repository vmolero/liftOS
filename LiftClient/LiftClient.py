import socket


class LiftClient:
  def __init__(self, id: int, startingFloor: int, weight: int):
    self.__id = id
    self.__floor = startingFloor
    self.__weight = weight
    
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
      busy = True
      #while busy:
      received = str(sock.recv(1024), "utf-8")
      if received == 'free':
        busy = False
        print("Status: Free")

      print("Received: {}".format(received))
      return True
    except ConnectionRefusedError:
      return False