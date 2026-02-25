import Pyro5.api


@Pyro5.api.expose
class EchoServer:
    def echo(self, message):
        print("message received", message)
        return f"Server received: {message}"


def main():
    daemon = Pyro5.api.Daemon()               # Create daemon
    ns = Pyro5.api.locate_ns()                # Locate name server
    uri = daemon.register(EchoServer)         # Register class
    ns.register("echo.server", uri)           # Register with name server

    print("Echo server is running...")
    daemon.requestLoop()                      # Start loop


if __name__ == "__main__":
    main()
