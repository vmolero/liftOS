# import sys
import os
from .LiftClient import LiftClient


lift_input = 'start;hi;end'
# input = sys.argv[1:]
commands = "".join(lift_input).split(';')
if commands[0] != 'start':
    os._exit(1)

i = 1
client = LiftClient()
lift_id = client.send_command('start')

while i < len(commands) and commands[i] != 'end':
    if client.send_command(commands[i]):
        i += 1
    else:
        print('Lift service unavailable')
        i = len(commands)

client.send_command('end')
