# IServer: Insult Server

import random
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class IS:
    def __init__ ( self ):
        self.insults   = []
        self.observers = []

    def add_insult ( self, insult ):
        self.insults.append(insult)
        self.notifyAll()
        return "added"

    def get_insults ( self ):
        return self.insults

    def insult_me ( self ):
        if not self.insults:
            return "no insults"
        return random.choice(self.insults)

    def subscribe ( self, observer ):
        self.observers.append(observer)

    def notifyAll ( self, insult ):
        for observer in self.observers:
            observer.update( insult )

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register a function
    server.register_instance(IS())

    # Run the server's main loop
    server.serve_forever()
