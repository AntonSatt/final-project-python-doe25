# Functions I use a lot
import os
import time
import sys
import main


# Clears the console for a better viewing experience
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Short timer
def short_timer(): 
    for i in range(1): # Change value to change timer speed
        print('.', end='',flush=True)
        time.sleep(1)

# To be able to press any key to continue on depending on what OS you run.
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

def wait_for_any_key_or_timeout(seconds):
    start_time = time.time()
    
    if sys.platform.startswith('win'):  # Windows
        import  msvcrt
        while time.time() - start_time < seconds:
            if msvcrt.kbhit():
                key = msvcrt.getch()  
                print("\nReturning to menu!")
                time.sleep(1)
                main.main()
            time.sleep(0.1)  
    
    else:  # Unix/Linux/macOS
        import termios
        import tty
        import select
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)  
            while time.time() - start_time < seconds:
                ready, _, _ = select.select([sys.stdin], [], [], 0.1)
                if ready:
                    key = sys.stdin.read(1)  # Read single character without Enter
                    print("\nReturning to menu!")
                    time.sleep(1)
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore terminal
                    main.main()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore terminal
