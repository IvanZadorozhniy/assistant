from Jarvis import Assistant

jarvis = Assistant()

while True:
    command = jarvis.listen()
    if command:
        is_done = jarvis.do_command(command=command)
    