#! python3

# Advent of Code Day 12

# Main Code

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

        
class system(object):

    def __init__(self,moons):
        self.moons = moons
##        self.max = 0
        self.time = 0

    def getMoons(self):
        return self.moons

    def getTime(self):
        return self.time

    def setTime(self,time):
        self.time = time
        return self.time

    def __str__(self):
        string = ''
        for moon in moons:
            string += str(moon) + '\n' #str(moon) might cause error

        return string

    def updateSystem(self,timesteps):

        while self.getTime() < timesteps:

            totalEnergy = 0

            for moon in self.getMoons():
                moon.updateV(self.getMoons())

            for moon in self.getMoons():
                moon.updateP()

            for moon in self.getMoons():
                totalEnergy += moon.getEnergy()

            self.setTime(self.getTime()+1)

##            print('After %s steps: \n%s' % (self.getTime(),self)) #- Self might return error
##            print('Total Enery: %s' % (totalEnergy))

        return self.getTime()
#Test Code - Working as intended
##moons = [moon([-1,0,2],[0,0,0]),moon([2,-10,-7],[0,0,0]),moon([4,-8,8],[0,0,0]),moon([3,5,-1],[0,0,0])]
##sys = system(moons)
##sys.updateSystem(10)


#Main Code

##file = open('aoc12.txt','r')

moons = [moon( [14,4,5],[0,0,0] ),moon( [12,10,8],[0,0,0] ),moon( [1,7,-10],[0,0,0] ),moon( [16,-5,3],[0,0,0] )]
sys = system(moons)
sys.updateSystem(1000)
