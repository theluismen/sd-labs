import Pyro5.api

def main():
    with Pyro5.api.Proxy("PYRONAME:insult.server") as s:
        print("Adding: Negrata - "  + s.add_insult("Negrata") )
        print("Adding: Sudaca - "   + s.add_insult("Sudaca") )
        print("Adding: Panchito - " + s.add_insult("Panchito") )
        print()

        print("Insultos:")
        for i, insult in enumerate(s.get_insults()):
            print(f" {i} -> {insult}")
        print()

        try:
            print("Insulto Random: " + s.insult_me())
            print()
        except Exception as e:
            print("Insulto Random: ", e)

if __name__ == "__main__":
    main()
