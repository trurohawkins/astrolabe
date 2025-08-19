def drawSolarSystem(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    cy = height // 2
    cx = width // 2
    stdscr.addstr(cy, cx, 'S')
    stdscr.refresh()
