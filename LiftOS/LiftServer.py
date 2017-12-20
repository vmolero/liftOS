import socketserver
from .OneLiftOSHandler import OneLiftOSHandler


class LiftServer:

    def __init__(self, ip: str, port: int):
        self.__server = socketserver.TCPServer((ip, port), OneLiftOSHandler)

    def run(self):
        self.__server.serve_forever()
