import socketserver
import threading


class LiftOSHandler(socketserver.StreamRequestHandler):

    def use(self):
        raise NotImplementedError("Please Implement `Handler::use` this method")

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        try:
            liftOS = self.use()
        except NotImplementedError as exception:
            print(str(exception))
        data = self.rfile.readline().strip()
        if data == 'start':
            liftOS.start()

        while False:
            pass
           # self.__data = self.rfile.readline().strip()
           # if len(self.__data) == 0:
           #     break
           # print(self.__data)
            # Likewise, self.wfile is a file-like object used to write back
            # to the client
           # self.wfile.write(self.__data.upper())
        self.wfile.write(bytes('free', 'ascii'))

        print("{} wrote:".format(self.client_address[0]))
        data = str(self.request.recv(1024), 'ascii')
        response = bytes("{}: {}".format(liftOS.name, data), 'ascii')
        self.request.sendall(response)
