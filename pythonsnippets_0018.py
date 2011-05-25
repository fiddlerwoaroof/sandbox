import SocketServer
from cPickle import loads, dumps

class EchoHandler(SocketServer.BaseRequestHandler):
  dct = dict(
      demoObject = (1,2,3,4,5),
      demoObject1 = set([1,2,3,4,5]),
      demoObject2 = dict(q=(1,2,3,4,5))
  )
  def handle(self):
    while 1:
      data = self.request.recv(1024)
      if not data: break
      result = {}
      for key in data.split():
          print key
          result[key] = self.dct.get(key, None)
      self.request.send(dumps(result))


EchoServer = SocketServer.TCPServer(("", 8881), EchoHandler)
EchoServer.serve_forever()