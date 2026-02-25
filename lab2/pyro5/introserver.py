import Pyro5.api

# Define a simple remote object
@Pyro5.api.expose
class MyRemoteObject:
    def __init__(self, name):
        self.name = name

    def greet(self, message):
        return f"{self.name} says: {message}"

    def add(self, a, b):
        return a + b

def main():
    # Create a Pyro daemon
    with Pyro5.api.Daemon() as daemon:
        # Locate the Pyro name server
        try:
            ns = Pyro5.api.locate_ns()
        except Exception as e:
            print(f"Error: Could not find Name Server. {e}")
            return

        # Register the remote object class with the daemon
        uri = daemon.register(MyRemoteObject("RemoteObject"))
        
        # Register the object with a name in the name server
        ns.register("example.remote.object", uri)
        
        print(f"Server URI: {uri}")
        print("Server is ready.")
        
        # Start the event loop
        daemon.request_loop()

if __name__ == "__main__":
    main()