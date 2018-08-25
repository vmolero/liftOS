from LiftOS.Lift import Lift
import threading
import time

class LiftOS(threading.Thread):

  def __init__(self, target):
    threading.Thread.__init__(self, target=target)
    self.__commands = []
    self.__current_floor = 0
    self.__lifts = [Lift(1, 4)]
  
  def start(self):
    self.__lock = threading.Lock()
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
  
  def call(self, floor, user):
    self.__lifts[0].move_to(int(floor))
    return "State: " + str(self.__lifts[0].get_status()) + " Floor: " + str(self.__lifts[0].get_position())
  
  def move(self, floor, userId):
    self.__lifts[0].move_to(int(floor))
    return "State: " + str(self.__lifts[0].get_status()) + " Floor: " + str(self.__lifts[0].get_position())
  
  def end(self, userId):
    return "END"
