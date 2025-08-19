from threading import *
from queue import *
from curses import *
from control import *

def main(stdscr):
    stdscr.nodelay(True)
    q = Queue()
    t = Thread(target = inputThread, args=(stdscr, q), daemon=True)
    t.start()

    stdscr.clear()
    #stdscr.addstr(0, 0, "Hello sexy Boi")
    while True:
        while not q.empty():
            key = q.get()
            if key == ord('q'):
                return
            stdscr.addstr(0, 0, f"pressed {chr(key)}")
            stdscr.refresh()

if __name__ == "__main__":
    wrapper(main)
