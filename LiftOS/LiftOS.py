from .Lift import Lift


class LiftOS:

    def __init__(self, floors, lift_number):
        self.__floors = floors
        self.__lift_number = lift_number
        self.__commands = []
        self.__current_floor = 0
        self.__lifts = []

    def command(self, command: str) -> bool:
        self.__commands.append(command)
        return True

    def get_commands(self) -> list:
        return self.__commands

    def add_lift(self, lift: Lift):
        self.__lifts.append(lift)

    def get_lifts(self) -> list:
        return self.__lifts
