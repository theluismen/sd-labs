# IObserver: Insult Observer

import sys
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from observer import Observer

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(( sys.argv[1], int(sys.argv[2]) ),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register a function
    server.register_instance(Observer(sys.argv[1], int(sys.argv[2])))

    # Run the server's main loop
    server.serve_forever()
