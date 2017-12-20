import LiftOS.LiftOSHandler
import LiftOS.Lift


class OneLiftOSHandler(LiftOS.LiftOSHandler):

    def use(self):
        return LiftOS.Lift(5, 1)

