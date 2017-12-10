import socketserver


class LiftOSHandler(socketserver.StreamRequestHandler):
    data = None
    liftos = None

    def __init__(self, liftos):
        self.data = None
        self.liftos = liftos

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        print("{} wrote:".format(self.client_address[0]))
        while True:
            self.data = self.rfile.readline().strip()
            if len(self.data) == 0:
                break;
            print(self.data)
            # Likewise, self.wfile is a file-like object used to write back
            # to the client
            self.wfile.write(self.data.upper())
