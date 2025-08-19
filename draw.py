from astro import *
import config

def debug(message):
    with open("debug.log", "a") as f:
        f.write(f"{message}\n")

def drawSolarSystem(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    cy = height // 2
    cx = width // 2

    stdscr.addstr(cy, cx, '☉')
    for planet_name, planet_data in config.solar_system.items():
        drawPlanet(planet_data, stdscr)
    stdscr.refresh()

def drawPlanet(planet, stdscr):
    height, width = stdscr.getmaxyx()
    cy = height // 2
    cx = width // 2
    for i in range(360):
        angle, distance, x, y = Planet_Position(i, planet["radius"], planet["width"], planet["height"], cx, cy, planet["angular_velocity"], 0)
        stdscr.addstr(int(y), int(x), '.')#planet["char"])
    angle, distance, x, y = Planet_Position(config.time, planet["radius"], planet["width"], planet["height"], cx, cy, planet["angular_velocity"], 0)
    stdscr.addstr(int(y), int(x), planet["char"])

