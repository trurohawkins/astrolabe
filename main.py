from curses import *
from time import *

import fileman
import config
from astro import *
from draw import *

def main(stdscr):
    curs_set(0)
    stdscr.nodelay(True)
    stdscr.clear()

    height, width = stdscr.getmaxyx()
    config.screenHeight = height
    config.screenWidth = width
    
    
    #stdscr.addstr(0, 0, "Hello sexy Boi")
    print(config.solar_system)
    while True:
        key = stdscr.getch()
        if key == ord('q'):
            return
        drawSolarSystem(stdscr)
        config.time += 1
        sleep(0.05)

if __name__ == "__main__":
    wrapper(main)
