import math
import os

#variantes
earth_gravity = 9.80665
moon_gravity = 1.625
mars_gravity = 3.72076
gravity_list = [earth_gravity,moon_gravity,mars_gravity]
choosen_gravity = gravity_list[player_gravity]

#fontions
def flight_time():
    global velocity
    global choosen_gravity
    global angle
    time = 2 * velocity * math.sin(angle) / choosen_gravity
    return time

def maximum_height(): 
    global velocity
    global choosen_gravity
    global angle
    height = (velocity ** 2 * math.sin(angle) ** 2) / (2 * choosen_gravity)
    return height

def horizontal_range():
   global choosen_gravity
   global angle
   global velocity
   x_range = (velocity ** 2 * math.sin(2 * angle)) / choosen_gravity
   return x_range

os.system('clear')