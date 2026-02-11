import xmlrpc.client
import sys

class Observer:
    def __init__ ( self, host, port ):
        self.host = host
        self.port = port
        self.s = xmlrpc.client.ServerProxy('http://localhost:8000')

    def subscribe ( self ):
        self.s.subscribe( self )

    def update ( self, insult ):
        return f"got {insult}"

# Main

o1 = Observer( sys.argv[1], sys.argv[2] )
o1.subscribe()

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(( sys.argv[1], sys.argv[2] ),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register a function
    server.register_instance(IS())

    # Run the server's main loop
    server.serve_forever()
