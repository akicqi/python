form urllib import urlopen
webpage = urlopen('http://akic.me')
text = webpage.read()

print text

from SocketServer import TCPServer,StreamRequestHandler

class Handler(StreamRequestHandler):
	def handle(self):
		addr = self.request.getpeername()
		print 'Got connection from'.addr
		self.wfile.write('Thank you for connecting')
	server = TCPServer(('',1234),Handle)
	server.serve_forever()