def drawSolarSystem(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    stdscr.addstr(int(height/2), int(width/2), 'S')
    stdscr.refresh()
