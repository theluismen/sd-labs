import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class Observer:
    def __init__ ( self, host, port ):
        self.host = host
        self.port = port
        self.s = xmlrpc.client.ServerProxy('http://localhost:8000')
        print( self.s.attach( self.host, self.port ) )

    def update ( self, insult ):
        print(f"got {insult}")
        return "insultau"
