# Functions I use a lot
import os
import time

# Clears the console for a better viewing experience
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Short timer
def short_timer():
    for i in range(3):
        print('.', end='',flush=True)
        time.sleep(1)