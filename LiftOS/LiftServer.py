from LiftOS.LiftOSHandler import LiftOSHandler
from LiftOS.LiftOS import LiftOS
from LiftOS.ThreadedTCPServer import ThreadedTCPServer


class LiftServer:

  def __init__(self, ip: str, port: int):
    self.__server = ThreadedTCPServer(
      (ip, port), 
      lambda *args, **keys: LiftOSHandler(self.callback, *args, **keys)
    )
    self.__liftOS = LiftOS(target=self)
    self.__liftOS.daemon = True
    self.__liftOS.start()

  def run(self):
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    # Exit the server thread when the main thread terminates

    print("Server loop running in thread:", self.__liftOS.name)
    self.__server.serve_forever()

  def parseAndRunCommand(self, rawCommand: str):
    parts = rawCommand.split(' ')
    operation = str(parts[0]).lower()
    idUser = parts[1]
    if operation == 'call':
      startingFloor = parts[2]
      weight = parts[3]
      return self.__liftOS.call(startingFloor, [idUser, weight])
    elif operation == 'move':
      nextFloor = parts[2]
      return self.__liftOS.move(nextFloor, idUser)
    else:
      return "end"

  def callback(self, data: str):
    return self.parseAndRunCommand(data)
    