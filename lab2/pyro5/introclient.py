import Pyro5.api

def main():
    try:
        # Locate the object using the name server URI shortcut
        # Pyro5 allows using "PYRONAME:name" directly in the Proxy constructor
        uri = "PYRONAME:example.remote.object"
        
        with Pyro5.api.Proxy(uri) as remote_object:
            # Bind the proxy to discover methods
            remote_object._pyroBind()

            # Call remote methods
            result = remote_object.greet("Hello from Pyro5 introspection!")
            print("Result of greet method:", result)

            result = remote_object.add(5, 10)
            print("Result of add method:", result)

            # Dynamically introspect the remote object
            # In Pyro5, remote methods are stored in _pyroMethods (set)
            print("\nAvailable methods on the remote object:")
            for method_name in sorted(remote_object._pyroMethods):
                print(f"- {method_name}")

    except Exception as e:
        print(f"Error during dynamic introspection: {e}")

if __name__ == "__main__":
    main()