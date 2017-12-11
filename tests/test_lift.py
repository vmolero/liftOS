import unittest
from liftOS.Lift import Lift
from liftOS.LiftState import LiftState


class TestLift(unittest.TestCase):
    __lift = None

    def setUp(self):
        self.__lift = Lift(0, 1)

    def test_idle(self):
        assert self.__lift.get_status() == LiftState.IDLE

    def test_moving(self):
        self.__lift.move_to(1)
        assert self.__lift.get_status() == LiftState.IDLE

    def test_get_position(self):
        assert self.__lift.get_position() == 0

    def test_call_1st_floor(self):
        self.__lift.move_to(1)
        assert self.__lift.get_position() == 1

    def test_call_current_floor(self):
        self.__lift.move_to(0)
        assert self.__lift.get_position() == 0
