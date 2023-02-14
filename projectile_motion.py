import math
import os

#variables
earth_gravity = 9.80665
moon_gravity = 1.625
mars_gravity = 3.72076
gravity_list = [earth_gravity, moon_gravity, mars_gravity]

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


os.system("cls")
player_gravity = int(input("Type 1 for Earth gravity simulation, 2 for Moon and 3 for Mars: ")) - 1
angle = math.radians(float(input("Enter the angle of the launch (in degrees): ")))
velocity = float(input("Enter the initial velocity of the lunch (in meters per second): "))
choosen_gravity = gravity_list[player_gravity]

FlightTime = float(round(flight_time(),2))
MaximumHeight = float(round(maximum_height(),2))
HorizontalRange = float(round(horizontal_range(),2))

print("The total flight time is %s seconds, the maximum height reached is %s meters and the distance traveled is %s meters" % (FlightTime,MaximumHeight,HorizontalRange))
if player_gravity == 0:
    if MaximumHeight <= 12000:
        print("your object is still in the troposphere")
    elif MaximumHeight > 12000 and MaximumHeight <= 50000:
        print("Your projectile has reached the stratosphere")   
    elif MaximumHeight > 50000 and MaximumHeight <= 80000:
        print("your projectile has reached the mesosphere")
    elif MaximumHeight > 80000 and MaximumHeight <= 700000:
        print("your projectile has reached the thermosphere")
    elif MaximumHeight > 700000 and MaximumHeight <= 10000000:
        print("your projectile has reached the exosphere")
    else:
        print("your projectile is really far away")