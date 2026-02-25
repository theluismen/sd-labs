import Pyro5.api
import random

@Pyro5.api.expose
class InsultServer:
    def __init__ ( self ):
        self.insults   = []

    def add_insult ( self, insult ):
        self.insults.append(insult)
        return "added"

    def get_insults ( self ):
        return self.insults

    def insult_me ( self ):
        if not self.insults:
            raise ValueError("No Insults")
        return random.choice(self.insults)

def main():
    daemon = Pyro5.api.Daemon()               # Create daemon
    ns     = Pyro5.api.locate_ns()            # Locate name server
    uri    = daemon.register(InsultServer)    # Register class
    ns.register("insult.server", uri)         # Register with name server

    print("Insult Server is running...")
    daemon.requestLoop()                      # Start loop

if __name__ == "__main__":
    main()
