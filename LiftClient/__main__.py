import sys
import os
from .LiftClient import LiftClient

commands = "".join(sys.argv[1:]).split(';')
if commands[0] != 'start':
    os._exit(1)

i = 1
client = LiftClient()
while i < len(commands) and commands[i] != 'end':
    client.send_command(commands[i])
    i += 1
