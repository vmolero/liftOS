from LiftOS.OneLiftOSHandler import OneLiftOSHandler
from LiftOS.LiftOS import LiftOS
from LiftOS.ThreadedTCPServer import ThreadedTCPServer


class LiftServer:

    def __init__(self, ip: str, port: int):
        self.__server = ThreadedTCPServer((ip, port), OneLiftOSHandler)
        self.__liftOS = LiftOS(target=self)
        self.__liftOS.daemon = True
        self.__liftOS.start()

    def run(self):
        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        # Exit the server thread when the main thread terminates

        print("Server loop running in thread:", self.__liftOS.name)
        self.__server.serve_forever()
