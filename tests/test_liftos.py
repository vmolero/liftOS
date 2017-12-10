import unittest
from liftOS import LiftOS
from liftOS import Lift


class TestLiftOS(unittest.TestCase):
    liftOS = None

    def setUp(self):
        self.liftOS = LiftOS.LiftOS(2, 1)

    def test_receive_command(self):
        command = "CALL 1"
        self.liftOS.command(command)
        assert "CALL 1" in self.liftOS.get_commands()

    def test_add_lift(self):
        lift1 = Lift.Lift("A", 1)
        self.liftOS.add_lift(lift1)
        assert lift1 in self.liftOS.get_lifts()