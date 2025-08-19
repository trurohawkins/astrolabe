from threading import *
from queue import *
from curses import *
from control import *
from astro import *
from draw import *

def main(stdscr):
    stdscr.nodelay(True)
    q = Queue()
    t = Thread(target = inputThread, args=(stdscr, q), daemon=True)
    t.start()

    #stdscr.clear()
    #stdscr.addstr(0, 0, "Hello sexy Boi")
    while True:
        while not q.empty():
            key = q.get()
            if key == ord('q'):
                return
        drawSolarSystem(stdscr)

if __name__ == "__main__":
    wrapper(main)
