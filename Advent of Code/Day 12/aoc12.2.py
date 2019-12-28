#! python3

# Advent of Code Day 12

# Main Code

import numpy as np
from math import gcd
from functools import reduce

##def LCM(list):
##    lcm = list[0]
##    for i in list[1:]:
##        lcm = lcm*i/gcd(lcm,i)
##    return lcm
def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

class moon(object):

    def __init__(self,position,velocity):
        ''' Intializes an object, moon with a list of its position and velocity in [x,y,z]'''
        self.pos = position
        self.vel = velocity

    def getPosition(self):
        return self.pos

    def getVelocity(self):
        return self.vel

    def getX(self):
        return self.getPosition()[0]
    
    def getY(self):
        return self.getPosition()[1]
    
    def getZ(self):
        return self.getPosition()[2]

    def getXV(self):
        return self.getVelocity()[0]

    def getYV(self):
        return self.getVelocity()[1]

    def getZV(self):
        return self.getVelocity()[2]
    
    def setPosition(self,position):

##        if value == 'x':
##            self.pos[0] = position
##
##        elif value == 'y':
##            self.pos[1] = position
##
##        elif value == 'z':
##            self.pos[2] = position
        self.pos = position
            
        return self.pos

    def setVelocity(self,velocity,value):
        
        if value == 'x':
            self.vel[0] = velocity
        elif value == 'y':
            self.vel[1] = velocity
        elif value == 'z':
            self.vel[2] = velocity
        return self.vel

    def getEnergy(self):
        energy = ( abs(self.getPosition()[0])+abs(self.getPosition()[1])+abs(self.getPosition()[2]) ) * (abs(self.getVelocity()[0])+abs(self.getVelocity()[1])+abs(self.getVelocity()[2]))
        return energy

    def __str__(self):

        string = 'pos : x = %s, y = %s, z = %s , vel : x = %s, y = %s,z = %s' % (self.getPosition()[0],self.getPosition()[1],self.getPosition()[2],self.getVelocity()[0],self.getVelocity()[1],self.getVelocity()[2])
        return string

    def updateV(self,moons):

        for moon in moons:

##          Updates velocity
            
            if moon.getX() < self.getX():
                self.setVelocity(self.getXV()-1,'x')
            elif moon.getX() > self.getX():
                self.setVelocity(self.getXV()+1,'x')

            if moon.getY() < self.getY():
                self.setVelocity(self.getYV()-1,'y')
            elif moon.getY() > self.getY():
                self.setVelocity(self.getYV()+1,'y')

            if moon.getZ() < self.getZ():
                self.setVelocity(self.getZV()-1,'z')
            elif moon.getZ() > self.getZ():
                self.setVelocity(self.getZV()+1,'z')

    def updateP(self):
        
##      Updates Position
        
        newX = self.getX() + self.getXV()
        newY = self.getY() + self.getYV()
        newZ = self.getZ() + self.getZV()

        self.setPosition([newX,newY,newZ])
        return self.getPosition()

##    def updateIndiv(self,int):
##
##        if int == 0:
##            
##            if moon.getX() < self.getX():
##                self.setVelocity(self.getXV()-1,'x')
##            elif moon.getX() > self.getX():
##                self.setVelocity(self.getXV()+1,'x')
##
##            new = self.getX() + self.getXV()
##
##        if int == 1:
##            
##            if moon.getY() < self.getY():
##                self.setVelocity(self.getYV()-1,'y')
##            elif moon.getX() > self.getX():
##                self.setVelocity(self.getYV()+1,'y')
##
##            new = self.getY() + self.getYV()
##
##        if int == 2:
##            
##            if moon.getZ() < self.getZ():
##                self.setVelocity(self.getZV()-1,'z')
##            elif moon.getX() > self.getX():
##                self.setVelocity(self.getZV()+1,'z')
##
##            new = self.getZ() + self.getZV()
##
##        return new
    
class system(object):

    def __init__(self,moons):
        self.moons = moons
##        self.max = 0
        self.time = 0
        self.initialEnergy = 0
        self.initalSelf = str(self)
        self.initialX = []
        self.initialY = []
        self.initialZ = []
        self.period = {'x':0,'y':0,'z':0}

        for moon in moons:
            self.initialEnergy += moon.getEnergy()
            self.initialX.append(moon.getX())
            self.initialY.append(moon.getY())
            self.initialZ.append(moon.getZ())

    def getMoons(self):
        return self.moons

    def getTime(self):
        return self.time

    def setTime(self,time):
        self.time = time
        return self.time

    def __str__(self):
        string = ''
        for moon in self.getMoons():
            string += str(moon) + '\n' #str(moon) might cause error

        return string

    def getList(self,xyz):

        list = []
        if xyz == 'x':
##            list = []
            for moon in self.getMoons():
                list.append(moon.getX())

        elif xyz == 'y':
##            list = []
            for moon in self.getMoons():
                list.append(moon.getY())

        elif xyz == 'z':
##            list = []
            for moon in self.getMoons() :
                list.append(moon.getZ())
        return list

    def updateSystem(self):

        breakCondition = [False,False,False]
        while breakCondition != [True,True,True]:
##        while True:
            
            totalEnergy = 0

            for moon in self.getMoons():
                moon.updateV(self.getMoons())

            for moon in self.getMoons():
                moon.updateP()

            for moon in self.getMoons():
                totalEnergy += moon.getEnergy()

            self.setTime(self.getTime()+1)


            if self.getList('x') == self.initialX:
                if moons[0].getXV() == 0 and moons[1].getXV() == 0 and moons[2].getXV() == 0 and moons[3].getXV() == 0:
                    print('X period found at: %s' % (self.getTime()))
                    self.period['x'] = self.getTime()
                    breakCondition[0] = True

            elif self.getList('y') == self.initialY:
                if moons[0].getYV() == 0 and moons[1].getYV() == 0 and moons[2].getYV() == 0 and moons[3].getYV() == 0:
                    print('Y period found at: %s' % (self.getTime()))
                    self.period['y'] = self.getTime()
                    breakCondition[1] = True

            elif self.getList('z') == self.initialZ:
                if moons[0].getZV() == 0 and moons[1].getZV() == 0 and moons[2].getZV() == 0 and moons[3].getZV() == 0:
                    print('Z period found at: %s' % (self.getTime()))
                    self.period['z'] = self.getTime()
                    breakCondition[2] = True
                    

            if self.getTime() % 100000 == 0:
                print('Current time at: %s' % (self.getTime()))

            if totalEnergy == self.initialEnergy:
                if str(self) == self.initalSelf:
                    print('Copy found at %s timestep' % (self.getTime()))
                    return self.getTime()

##            print('After %s steps: \n%s' % (self.getTime(),self)) #- Self might return error
##            print('Total Enery: %s at time %s' % (totalEnergy,self.getTime())) $- Working as intended

        return self.period
##Test Code - Working as intended
##moons = [moon([-1,0,2],[0,0,0]),moon([2,-10,-7],[0,0,0]),moon([4,-8,8],[0,0,0]),moon([3,5,-1],[0,0,0])]
##sys = system(moons)
##m = sys.updateSystem()
##print(m)
##list = [m['x'],m['y'],m['z']]
##print(np.lcm.reduce(list))


#Main Code

##file = open('aoc12.txt','r')

moons = [moon( [14,4,5],[0,0,0] ),moon( [12,10,8],[0,0,0] ),moon( [1,7,-10],[0,0,0] ),moon( [16,-5,3],[0,0,0] )]
sys = system(moons)
m = sys.updateSystem()
print(m)
list = [m['x'],m['y'],m['z']]
##print(list)
print(lcm(list))

## Interesting to note, it was really hard to find something that could give the proper LCM. numpy's lcm function didn't seem to work, and sometimes even returned a negative number as the answer. Got the current function from stackoverflow.
