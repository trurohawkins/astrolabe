from curses import *

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Hello sexy Boi")
    stdscr.refresh()
    stdscr.getkey()

if __name__ == "__main__":
    wrapper(main)
