import socketserver
import threading

class LiftOSHandler(socketserver.StreamRequestHandler):
  # @see https://stackoverflow.com/questions/5480456/proper-way-to-add-functionality-to-handle-in-a-python-tcp-server#5480999
  def __init__(self, callback, *args, **keys):
    self.callback = callback
    socketserver.BaseRequestHandler.__init__(self, *args, **keys)

  def handle(self):
    # self.rfile is a file-like object created by the handler;
    # we can now use e.g. readline() instead of raw recv() calls
    data = str(self.rfile.readline().strip(), 'utf-8')
    response = bytes(self.callback(data), 'utf-8')
    self.request.sendall(response)