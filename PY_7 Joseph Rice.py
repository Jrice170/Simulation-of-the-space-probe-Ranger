# Joseph Rice
# 3/8/2018
# PY 7 Energy 

from __future__ import division
from visual import * 
from visual.graph import * 

# intal conditions 
Earth = sphere(pos=vector(-2E8,0,0),radius=6.4E6,material=materials.earth,mass=6E24)
Moon = sphere(pos=vector(2E8,0,0),radius=1.75E6,mass=7E22)
Ranger = sphere(pos=vector(Earth.pos.x+Earth.radius+50,0,0),radius=1000000*1.4,color=color.blue,make_trail=True,mass=173)
## minimun inital speed
Ranger.p = vector(12000,0,0)*Ranger.mass # kg*m/s

Graph1 = gdisplay(x=0,y=0, width=600,height=150,title="Kinetic Energy 'Blue'; Graviational Kinetic Energy 'Red'; Total energy 'green' ",\
                  xtitle="Distance relative to earth (m)",ytitle="Energy (J)",foreground=color.white,background=color.black) 
KE = gcurve(color=color.orange)
PE = gcurve(color=color.red)
C = gcurve(color=color.green)



print("inital speed: ",Ranger.p/Ranger.mass, "m/s")
print("Earths mass ",Earth.mass,' kg')
print("Moon's mass ",Moon.mass," kg")
print("Ranger's mass: ",Ranger.mass,' kg')


G = 6.7E-11 # N*m^2/kg^2

# ranger 50m above earth
def seconds_to_days(t):
    """ converts seconds to days"""
    value = t/60/60/24
    return value

def force(object1,object2):
    """ object1 by object 2 gravitational force"""
    relative_position = object1.pos - object2.pos
    mage = mag(relative_position)
    rhat = relative_position/ mage
    Fmag = G*object1.mass*object2.mass/mage**2
    Force = -rhat*Fmag
    return Force
def position(object):
    """ Returns of outside of object """
    value = object.pos.x + object.radius
    return value
def square(value,value2):
    V = mag(value)/value2
    return V**2
def percent(value,value2):
    """returns a percent value"""
    top,botton=abs(value-value2),(value+value2)/2
    percent = top/botton*100
    return abs(percent)
    
 ## Time step of about 1 second
delta = 2 # s

## starting gravtational force by Earth 
F_by_earth = force(Ranger,Earth) # N 
## starting gravtational force by moon
F_by_mooon = force(Ranger,Moon) # N 

# starting value of t
t=0  
Work = 0 #J 
KEi = 0.5*Ranger.mass*square(Ranger.p,Ranger.mass) # J inital 
while True:
    
    F_earth = force(Ranger,Earth)
    F_Moon = force(Ranger,Moon)
    # update forces
    Fnet = F_earth + F_Moon
    # update momentum
    
    Ranger.p = Ranger.p + Fnet*delta
    # update position
    Ranger.pos = Ranger.pos + (Ranger.p/Ranger.mass)*delta

    ## calcutations for KE and U gravity
    Distance = mag(Ranger.pos-Earth.pos)
    Distance2 = mag(Ranger.pos-Moon.pos) 
    U = -G*Ranger.mass*Earth.mass/Distance + -G*Ranger.mass*Moon.mass/Distance2
    Dr = (Ranger.p/Ranger.mass)*delta
    Work = Work +  dot(Fnet,Dr)
    K = 0.5*Ranger.mass*square(Ranger.p,Ranger.mass)
    # plot Data 
    KE.plot( pos=(t,K) )
    PE.plot( pos=(t,U) )
    C.plot( pos=(t,K+U))
    t=t +  delta
    # stops loop 
    if position(Ranger) >= Moon.pos.x:
        break
    
print("\n")
print("The impact velocity is: ", Ranger.p/Ranger.mass, ' m/s')
print("The trip time: ", seconds_to_days(t), ' days')
print("\n")
print("___________...........__________")
print("\n")
print("Total Energy: ",K+U, "J")
print("Kinetic Energy Final= ", "%.4g" %K, 'J')
print("Kinetic Energy inital= ", "%.4g" %KEi, "J")
c = K-KEi
print("\n")
print("Chance in Kinetic Energy= ", "%.4g" %c, "J")
print(" Amount of Work= ","%.4g" %Work, "J" )
print("percent diff %   ", round(percent(Work,c),3), ' %')


