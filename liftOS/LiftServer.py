import socketserver
from liftOS import LiftOS
from liftOS import LiftOSHandler


class LiftServer:
    server = None

    def __init__(self):
        self.server = socketserver.TCPServer(("localhost", 9999), LiftOSHandler(LiftOS))

    def run(self):
        self.server.serve_forever()
