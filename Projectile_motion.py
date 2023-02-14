#import the math module
import math
#import the os module (used to control the system)
import os
#import the matplotlib.pyplot module as the name of plt (used to make graphs with data)
import matplotlib.pyplot as plt

#variables used to simulate the gravity on the Earth, the Moon and Mars
earth_gravity = 9.80665
moon_gravity = 1.625
mars_gravity = 3.72076
gravity_list = [earth_gravity, moon_gravity, mars_gravity]
time = 0.00

#calculate the X axis position using the velocity, the time, the angle and the gravity
def x_pos():
    XPos = velocity * time * math.cos(angle)
    return XPos
#calculate the Y axis position using the velocity, the time, the angle and the gravity
def y_pos():
    YPos = velocity * time * math.sin(angle) - (choosen_gravity * time ** 2)/2
    return YPos
#calculate the time spend in the air
def flight_time():
    global velocity
    global choosen_gravity
    global angle
    FlightTime = 2 * velocity * math.sin(angle) / choosen_gravity
    return FlightTime
#calculate the height at the peak height of the projectile
def maximum_height(): 
    global velocity
    global choosen_gravity
    global angle
    height = (velocity ** 2 * math.sin(angle) ** 2) / (2 * choosen_gravity)
    return height
#calculate the diastance achieved by the projectile
def horizontal_range():
   global choosen_gravity
   global angle
   global velocity
   x_range = (velocity ** 2 * math.sin(2 * angle)) / choosen_gravity
   return x_range
#calculate the best range achievable (using an angle of 45 degrees)
def best_range():
   global choosen_gravity
   global angle
   global velocity
   BestRange = (velocity ** 2 * math.sin(2 * 0.785398)) / choosen_gravity
   return BestRange
#calculate the highest height possible (using an angle of 90 degrees)
def best_height(): 
    global velocity
    global choosen_gravity
    global angle
    best_height = (velocity ** 2 * math.sin(1.5708) ** 2) / (2 * choosen_gravity)
    return best_height

os.system("clear")
#get the gravity the player want to use
player_gravity = int(input("Type 1 for Earth gravity simulation, 2 for Moon and 3 for Mars: ")) - 1
#translate the degrees to radiants
angle = math.radians(float(input("Enter the angle of the launch (in degrees): ")))
#translate the speed from km/h to meters per second
velocity = float(input("Enter the initial velocity of the lunch (in km/h): ")) / 3.6
#take the corresponding gravity value from a list of gravity
choosen_gravity = gravity_list[player_gravity]
#round the value of the function and format it to have a comma each 3 "int" digits
FlightTime = "{:,}".format(float(round(flight_time(),3)))
MaximumHeight = "{:,}".format(float(round(maximum_height(),3)))
HorizontalRange = "{:,}".format(float(round(horizontal_range(),3)))

print("The total flight time is %s seconds, the maximum height reached is %s meters and the distance traveled is %s meters" % (FlightTime,MaximumHeight,HorizontalRange))

#calculate the maximum height
MaximumHeight = maximum_height()
#calculate the total flight time
FlightTime = flight_time()

#print the astmosphere the projectile is in using the maximum height the projectile can achieve
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

#set a variable for the time to register the current time spend in the simulation to get the X and Y position
time = 0.00

#create the lists to register every x and y pos for every 1/100 of a second
XPos_lst = []
YPos_lst = []

#enter the x and y pos of every 1/100 of a second
MaxRange = best_range()
BestHeight = best_height()
while True:
    MaxRange = best_range()
    BestHeight = best_height()
    YPos = y_pos()
    XPos = x_pos()
    XPos_lst.append(XPos)
    YPos_lst.append(YPos)
    time += 0.01
    if time >= FlightTime:
        break

#use matplotlib to plot (add data) to the graph and show the graph
plt.plot(XPos_lst,YPos_lst)
#change the x axis label
plt.xlabel("Projectile distance")
#change the y axis label
plt.ylabel("Projectile height")
#set the range of the graph knowing the highest height possibly achieved and the farthest distance possibly achieved
plt.xlim(left=0)
plt.xlim(right=MaxRange)
plt.ylim(bottom=0)
plt.ylim(top=BestHeight)
#change the title by the planet witch the simulation is happening on
if player_gravity == 0:
    plt.title("Earth simulation")
elif player_gravity == 1:
    plt.title("Moon simulation")
else:
    plt.title("Mars simulation")

#show the diagram by creating a new window
plt.show()