from .LiftServer import LiftServer


def main():
    server = LiftServer("localhost", 9999)
    server.run()


main()
