#! python3

# Advent of Code Day 6

#TODO: Create the planets based on the orbits

file = open('aoc6.txt','r')

#Test Input
##file = open('aoc6test.txt','r')

inputList = file.readlines()

file.close()

planetDict = {}

for input in inputList:

##    print('Input is %s' % (input)) #- Working as intended
    input = input.strip('\n')
    planets = input.split(')')
##    print('The planet %s is orbiting %s' % (planets[1],planets[0])) #- Working as intended

    if planets[0] not in planetDict.keys():

        planetDict[planets[0]] = [planets[1]]
##        print('Planet Orbit created') #- Working as intended

    else:

        planetDict.get(planets[0]).append(planets[1])
##        print('Planet Orbit updated') #- Working as intended

    if planets[1] not in planetDict.keys():

        planetDict[planets[1]] = []

##print(planetDict) #- Working as intended

#Iterate through the planets in a psuedo DFS method (using dictionaries?)
#Find totoal no, of iterations.

def orbitCount(dictionary,planet):
    '''Returns the number of planets the planet directly and indirectly orbits'''

    #Remember the Termination Case

    initialCount = 0
##    finalCount = 0
    currentPlanet = planet

    while currentPlanet != 'COM':

        initialCount += 1
        currentPlanet = getParentPlanet(dictionary,currentPlanet)

##    print('Reached COM, current count of planet %s is: %s ' % (planet,initialCount)) #- Working as intended

    return initialCount

##    for int in range(initialCount+1):
##
##        finalCount += int
##
##    print('Calculations complete: Final Count - %s' % (finalCount))
##    return finalCount

def getParentPlanet(dictionary,planet):
    '''Finds the planet that the target planet is currently orbiting'''

    for thing in dictionary:

        for i in dictionary.get(thing):

            if i == planet:

##                print('Parent planet found: %s ' % (thing)) #- Working as intended
                return thing


    print('Error: Planet not found')
    assert False


def main():

    totalCount = 0

    for planet in planetDict:

        totalCount += orbitCount(planetDict,planet)

    print('Program Complete.')
    return totalCount


print(main())

## Initlal Output - 102232 (too low)
