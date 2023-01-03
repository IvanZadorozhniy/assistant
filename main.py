'''run programm'''
from jarvis import Assistant

jarvis = Assistant()

while True:
    command = jarvis.listen()
    if command:
        jarvis.do_command(command=command)
