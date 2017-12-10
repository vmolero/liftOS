from enum import Enum


class LiftState(Enum):
    IDLE = 0
    DOORS = 1
    MOVING = 2
