import math

Earth = {"name":"Earth", "char":'E', "height":1, "width":1, "radius":1, "velocity":0}

def Planet_Position(time,radius, height, width, origin_x, origin_y, angular_v, intial_phase):
    #Calculate planetary anagle relative to Sun 
    solar_angle = angular_v * time + intial_phase

    #Calculate x,y coordiantes
    planet_x = origin_x + radius * width  * math.cos(solar_angle)
    planet_y = origin_y + radius * height * math.sin(solar_angle)

    #Calculate distance from Sun
    solar_distance = math.sqrt( ( planet_x**2 ) + ( planet_y**2) )

    return (solar_angle, solar_distance, planet_x, planet_y)
    
