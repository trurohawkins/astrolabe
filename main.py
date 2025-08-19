from curses import *
from time import *

from astro import *
from draw import *

def main(stdscr):
    curs_set(0)
    stdscr.nodelay(True)
    stdscr.clear()
    #stdscr.addstr(0, 0, "Hello sexy Boi")
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            return
        drawSolarSystem(stdscr)
        sleep(0.05)

if __name__ == "__main__":
    wrapper(main)
