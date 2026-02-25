import Pyro5.api

@Pyro5.api.expose
@Pyro5.api.behavior(instance_mode="single")
class Observable:
    def __init__(self):
        self.observers = []  # List to store observer proxies

    def register_observer(self, observer_uri):
        """Register an observer using its remote URI."""
        # Convert URI into a Pyro proxy to call its methods later
        observer_proxy = Pyro5.api.Proxy(observer_uri)
        self.observers.append(observer_proxy)
        print(f"✅ Observer {observer_uri} registered.")

    def notify_observers(self, message):
        """Notify all registered observers."""
        print(f"📢 Notifying {len(self.observers)} observers...")
        
        # Iterate over a copy to allow removal during iteration if needed
        for observer in list(self.observers):
            try:
                observer.update(message)  # Remote method call
            except Exception:
                print(f"❌ Observer unreachable. Removing from list.")
                self.observers.remove(observer)

def main():
    with Pyro5.api.Daemon() as daemon:
        try:
            ns = Pyro5.api.locate_ns()
        except Exception as e:
            print(f"Error: Name Server not found. {e}")
            return

        uri = daemon.register(Observable)
        ns.register("example.observable", uri)
        
        print(f"Observable server is running. URI: {uri}")
        daemon.request_loop()

if __name__ == "__main__":
    main()