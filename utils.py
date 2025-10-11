'''
Small functions that are easlily called from here to do something.
'''
import os
import time
import sys

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def timer_short(): 
    for i in range(1): # Change value to change timer speed
        print('.', end='',flush=True)
        time.sleep(1)

def press_any_key(prompt='Press any key to continue...'):
    if os.name == 'nt': # Windows
        import msvcrt
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