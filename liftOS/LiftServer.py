import socketserver
from LiftOSHandler import LiftOSHandler
from LiftOS import LiftOS


class LiftServer:
    server = None

    def __init__(self):
        self.server = socketserver.TCPServer(("localhost", 9999), LiftOSHandler(LiftOS))

    def run(self):
        self.server.serve_forever()
