from LiftOS.LiftOSHandler import LiftOSHandler
from LiftOS.Lift import Lift


class OneLiftOSHandler(LiftOSHandler):

    def use(self):
        return Lift(5, 1)

