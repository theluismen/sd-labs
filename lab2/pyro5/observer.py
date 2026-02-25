import Pyro5.api

@Pyro5.api.expose
class Observer:
    def update(self, message):
        """This method is called when the observable sends a notification."""
        print(f"🔔 Received update: {message}")

def main():
    # 1. Locate the subject
    try:
        ns = Pyro5.api.locate_ns()
        observable_uri = ns.lookup("example.observable")
    except Exception as e:
        print(f"Could not connect to Name Server or Subject: {e}")
        return

    # 2. Start local daemon to receive callbacks
    with Pyro5.api.Daemon() as daemon:
        observer_instance = Observer()
        # Register the local observer to get a URI
        my_uri = daemon.register(observer_instance)
        
        # 3. Register our URI with the remote Subject
        with Pyro5.api.Proxy(observable_uri) as observable:
            observable.register_observer(my_uri)
        
        print(f"Observer registered and waiting for notifications...")
        daemon.request_loop()

if __name__ == "__main__":
    main()