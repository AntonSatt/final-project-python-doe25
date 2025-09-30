# Functions I use a lot
import os
import time
import sys


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

# To be able to press any key to continue on depending on what OS you run.
def press_any_key(prompt='Press any key to continue...'):
    if os.name == 'nt': # Windows
        import msvcrt;
        def wait():
            print("Press any key to continue")
            msvcrt.getch()
    else: # Unix (Linux & Mac)
        import tty
        import termios
        """reads a single character"""
        sys.stdout.write(prompt)
        sys.stdout.flush()
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

