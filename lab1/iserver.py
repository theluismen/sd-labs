# IServer: Insult Server

import random
import xmlrpc.client
from observer import Observer
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class InsultServer:
    def __init__ ( self ):
        self.insults   = []
        self.observers = []

    def add_insult ( self, insult ):
        self.insults.append(insult)
        self.notifyAll(insult)
        return "added"

    def get_insults ( self ):
        return self.insults

    def insult_me ( self ):
        if not self.insults:
            return "no insults"
        return random.choice(self.insults)

    def attach ( self, host, port ):
        observer = xmlrpc.client.ServerProxy(f"http://{host}:{port}")
        self.observers.append(observer)
        return "attached"

    def notifyAll ( self, insult ):
        for observer in self.observers:
            print( observer.update( insult ) )
        return "notified"

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register a function
    server.register_instance(InsultServer())

    # Run the server's main loop
    server.serve_forever()
