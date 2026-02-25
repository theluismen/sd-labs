import Pyro5.api


def main():
    with Pyro5.api.Proxy("PYRONAME:echo.server") as echo_server:
        response = echo_server.echo("HOLA")
        print(f"Response from server: {response}")


if __name__ == "__main__":
    main()
