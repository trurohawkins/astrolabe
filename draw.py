from astro import *

def drawSolarSystem(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    cy = height // 2
    cx = width // 2

    stdscr.addstr(cy, cx, 'S')
    drawPlanet(Earth, stdscr)

    stdscr.refresh()

def drawPlanet(planet, stdscr):
    height, width = stdscr.getmaxyx()
    cy = height // 2
    cx = width // 2

    angle, distance, x, y = Planet_Position(0, planet["radius"], 1, 1, cx, cy, planet["velocity"], 0)
    stdscr.addstr(int(y), int(x), planet["char"])
