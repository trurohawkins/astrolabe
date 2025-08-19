from astro import *
import config

def drawSolarSystem(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    cy = height // 2
    cx = width // 2

    stdscr.addstr(cy, cx, 'S')
#    drawPlanet(config.Mercury, stdscr)
#    drawPlanet(config.Earth, stdscr)

    for planet_name, planet_data in config.solar_system.items():
        drawPlanet(planet_data, stdscr)
    stdscr.refresh()

def drawPlanet(planet, stdscr):
    height, width = stdscr.getmaxyx()
    cy = height // 2
    cx = width // 2

#    angle, distance, x, y = Planet_Position(config.time, planet["radius"], planet["width"], planet["height"], cx, cy, planet["velocity"], 0)
    angle, distance, x, y = Planet_Position(config.time, planet["radius"], planet["width"], planet["height"], cx, cy, planet["angular_velocity"], 0)
    stdscr.addstr(int(y), int(x), planet["char"])
