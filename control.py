def inputThread(stdscr, q):
    while True:
        ch = stdscr.getch()
        if ch != -1:
            q.put(ch)
