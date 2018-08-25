import sys
import os
import time
from .LiftClient import LiftClient


lift_input = 'start;hi;end'
# inp = sys.argv[1:]
inp = input()
print(inp)
user = inp.split(' ')
userId = user[0]
startingFloor = user[1]
userWeight = user[2]
client = LiftClient(userId, startingFloor, userWeight)
n = int(input())
currentFloor = startingFloor
for _ in range(n):
  line = input()
  lineArgs = line.split(' ')
  nextFloor = lineArgs[0]
  timeToSleep = int(lineArgs[1])
  client.send_command('CALL ' + userId + ' ' + currentFloor + ' ' + userWeight)
  client.send_command('MOVE ' + userId + ' ' + nextFloor)
  currentFloor = nextFloor
  time.sleep(timeToSleep)
client.send_command('END ' + userId)