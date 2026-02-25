import Pyro5.api

def main():
    # Use the PYRONAME shortcut for easy lookup
    uri = "PYRONAME:example.observable"
    
    try:
        with Pyro5.api.Proxy(uri) as observable:
            message = "Hello, Pyro5 Observers!"
            print(f"Sending message: {message}")
            observable.notify_observers(message)
    except Exception as e:
        print(f"Error contacting Observable: {e}")

if __name__ == "__main__":
    main()