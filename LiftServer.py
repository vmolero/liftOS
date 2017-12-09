import socketserver
from LiftOSHandler import LiftOSHandler


class LiftServer:
    server = None

    def __init__(self):
        self.server = socketserver.TCPServer(("localhost", 9999), LiftOSHandler)

    def run(self):
        self.server.serve_forever()
