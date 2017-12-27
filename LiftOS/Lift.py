import time
from threading import Lock
from LiftOS.LiftState import LiftState


class Lift:

    def __init__(self, idl: str, speed: int):
        self.__lock = Lock()
        self.__id = idl
        self.name = "Lift" + str(idl)
        self.__speed = speed
        self.__floor = 0
        self.__state = LiftState.IDLE

    def get_position(self):
        return self.__floor

    def move_to(self, new_floor: int) -> int:
        self.__state = LiftState.DOORS
        time.sleep(self.__speed / 2)
        self.__state = LiftState.MOVING
        time.sleep(abs(self.__floor - new_floor))
        self.__state = LiftState.DOORS
        time.sleep(self.__speed / 2)
        self.__state = LiftState.IDLE
        self.__floor = new_floor
        return new_floor

    def get_status(self) -> LiftState:
        return self.__state

    def acquire(self):
        # print >> sys.stderr, "acquired", self
        # traceback.print_tb
        self.__lock.acquire()

    def release(self):
        # print >> sys.stderr, "released", self
        # traceback.print_tb
        self.__lock.release()
