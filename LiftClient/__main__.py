import sys
import os
from .LiftClient import LiftClient

#commands = "".join(sys.argv[1:]).split(';')
#if commands[0] != 'start':
#    os._exit(1)
commands = ['start', 'hi', 'end']
i = 0
client = LiftClient()

while i < len(commands) and commands[i] != 'end':
    if client.send_command(commands[i]):
        i += 1
    else:
        print('Ĺift service unavailable')
        i = len(commands)

