from astro import *
import config

def debug(message):
    with open("debug.log", "a") as f:
        f.write(f"{message}\n")

def drawChar(stdscr, x, y, c):
    if x >= 0 and y >= 0 and x < config.screenWidth and y < config.screenHeight:
        stdscr.addstr(y, x, c)

def drawSolarSystem(stdscr):
    stdscr.clear()
    cy = config.screenHeight // 2
    cx = config.screenWidth // 2

    drawChar(stdscr, cx, cy, '☉')
    for planet_name, planet_data in config.solar_system.items():
        drawPlanet(planet_data, stdscr)
    stdscr.refresh()

def drawPlanet(planet, stdscr):
    height, width = stdscr.getmaxyx()
    cy = height // 2
    cx = width // 2
    for i in range(720):
        angle, distance, x, y = Planet_Position(i, planet["radius"], planet["width"], planet["height"], cx, cy, planet["angular_velocity"], 0)
        drawChar(stdscr, int(x), int(y), '.')
    angle, distance, x, y = Planet_Position(config.time, planet["radius"], planet["width"], planet["height"], cx, cy, planet["angular_velocity"], 0)
    drawChar(stdscr, int(x), int(y), planet["char"])

