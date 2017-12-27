from LiftOS.Lift import Lift
import threading


class LiftOS(threading.Thread):

    def __init__(self, target):
        threading.Thread.__init__(self, target=target)
        self.__commands = []
        self.__current_floor = 0
        self.__lifts = []

    def run(self):
        pass

    def command(self, command: str) -> bool:
        self.__commands.append(command)
        return True

    def get_commands(self) -> list:
        return self.__commands

    def add_lift(self, lift: Lift):
        self.__lifts.append(lift)

    def get_lifts(self) -> list:
        return self.__lifts
