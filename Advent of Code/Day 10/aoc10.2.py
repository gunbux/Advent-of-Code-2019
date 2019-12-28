#! python3

# Advent of Code Day 10

def raytrace(location1,location2):
    '''Traces all rays from the edge of the map to the target asteroid location, and returns a list of asteroids that are in line of sight'''

##    print('check location: %s' % (str(location2)))
    delta_x = location2[0] - location1[0]
    delta_y = location2[1] - location1[1]
##    print('delta values are: %s,%s' % (delta_x,delta_y))
    
    abs_x = abs(delta_x)
    abs_y = abs(delta_y)
    raytracing_list = []

##    try:
##        ratio = delta_x/delta_y
##    except ZeroDivisionError:
##        ratio = 0

##    print('running')

    if abs_x >= abs_y:

##        print('running1')

        for i in range(abs_x + 1):

            xval = i

            if delta_x < 0:

                xval = -i

            if abs_y != 0:
                yval = xval * delta_y / delta_x #- Interesting?
            else:
                yval = 0
##            print('currently checking %s,%s' % (xval,yval))
            if yval == int(yval):

##                print('found location: (%s,%s)' % (str(xval), str(yval)))
                raytracing_list.append((xval,int(yval)))

    elif abs_y > abs_x:

##        print('running2')

        for i in range(abs_y + 1):

            yval = i

            if delta_y < 0:
                yval = -i

            xval = delta_x * yval / delta_y #- Interesting?

##            print('currently checking %s,%s' % (xval,yval))

            if xval == int(xval):

##                print('found location: (%s,%s)' % (str(xval), str(yval)))
                raytracing_list.append( (int(xval),yval) )
##    print(raytracing_list)
    return raytracing_list
                      
    
########    #TODO: Get manhattan distance from the location
########
########    location_x = location1[0]
########    location_y = location1[1]
########    ratio = location_x/location_y
########    checker = 0
########    raytracing_list = []
########    
########    #TODO: Find all locations on map that are in line of sight of location at the given vertex
########
########    for i in range(max(location_x,location_y)):
########
########        checker = i
########        
########        if max(location_x,location_y) == location_x:
########
########            check_y = checker/ratio
########            print('checking at location x: %s' % (str(checker)))
########
########            if check_y == int(check_y):
########
########                print('found location: (%s,%s)' % (str(checker),str(check_y)))
########                raytracing_list.append((checker,int(check_y)))
########
########        elif max(location_x,location_y) == location_y:
########
########            check_x = checker * ratio
########            print('checking at location y: %s' % (str(checker)))
########
########            if check_x == int(check_x):
########
########                print('found location: (%s,%s)' % (str(checker), str(check_x)))
########                raytracing_list.append((int(check_x),checker))
########
########    
########    #TODO: Append the last asteroid that is in LOS before reaching the target to the output list
########    
########    #Output:
########
########
########    return raytracing_list

def reader():

    file = open('aoc10.txt', 'r')
    #Test input
##    file = open('aoc10test.txt','r')
##    file = open('aoc10test2.txt','r')
    input = file.readlines()

    file.close()

    asteroid_list = []

##    print('input[0] is %s' % (input[0])) #- Working as intended
    map_size = (len(input[0]) - 1,len(input))

    for y in range(len(input)):

        for x in range(len(input[y])):

            if input[y][x] == '#':

##                print('asteroid found at %s, %s' % (x,y)) #- Working as intended
                asteroid_list.append( (x,y) )

        

    return asteroid_list,map_size

def check_asteroid(asteroid,asteroids,map_size):

    los = []

##    print('checking asteroid at %s' % (str(asteroid)))

    for target in asteroids:

        line = raytrace(asteroid,target)

        for location in line:
            position = ( asteroid[0]+location[0],asteroid[1]+location[1] )

            if position in asteroids and position != asteroid:

                if position not in los:
                    los.append( position )
                break
####    for x in range(map_size[0]):
######        print('raytracing from %s,%s)' % (x,0)) #- Working as intended
####        delta = raytrace(asteroid,(x,0))
####        peralta = raytrace(asteroid,(x,map_size[1]-1)) #-Problem here   
######        print(delta)
####        for location in delta:
####            position = ( asteroid[0]+location[0],asteroid[1]+location[1] )
######            print('position found 1: %s' % (str(position)))
####            if position in asteroids and position != asteroid:
######                print('asteroid found in los: %s' % (str(position))) #- Working as intended
####                if position not in los:
####                    los.append( position )
####                break
####
####        for location in peralta:
####            position = ( asteroid[0]+location[0],asteroid[1]+location[1] )
######            print('position found 2: %s' % (str(position)))
####            if position in asteroids and position != asteroid:
######                print('asteroid found in los: %s' % (str(position))) #- Working as intended
####                if position not in los:
####                    los.append( position )
####                break
####
############################################
####                
####    for y in range(map_size[1]):
######        print('raytracing from %s,%s)' % (0,y)) #- Working as intended
####        delta = raytrace(asteroid,(0,y))
####        peralta = raytrace(asteroid,(map_size[0]-1,y))
######        print(delta)
######        print(peralta)
####        for location in delta:
####            position = ( asteroid[0]+location[0],asteroid[1]+location[1] )
######            print('position found 1: %s' % (str(position)))
####            if position in asteroids and position != asteroid:
######                print('asteroid found in los: %s' % (str(position))) #- Working as intended
####                if position not in los:
####                    los.append( position )
####                break
####
####        for location in peralta:
####            position = ( asteroid[0]+location[0],asteroid[1]+location[1] )
######            print('position found 1: %s' % (str(position)))
####            if position in asteroids and position != asteroid:
######                print('asteroid found in los: %s' % (str(position))) #- Working as intended
####                if position not in los:
####                    los.append( position )
####                break
    return los 

def vaporize(asteroid,asteroids,map_size):

    rel_location = (asteroid[0],0)
    asteroid_list = asteroids[:]
    destroyed = []

    while len(asteroid_list) > 1:

        print('checking location: %s' % (str(rel_location)))
        list = raytrace(asteroid,rel_location)

        for i in list:
            position = ( asteroid[0]+i[0],asteroid[1]+i[1] )

            if position in asteroid_list and position != asteroid:
                asteroid_list.remove(position)
                destroyed.append(position)
                print('remaining asteroids: %s' % (str(asteroid_list)))

        if rel_location[1] == 0:

            if rel_location[0] == map_size[0] - 1:
                rel_location = (rel_location[0],rel_location[1]+1)
            else:
                rel_location = (rel_location[0]+1,0)

        elif rel_location[0] == map_size[0] - 1:

            if rel_location[1] == map_size[1] - 1:
                rel_location = (rel_location[0] -1 , rel_location[1])
            else:
                rel_location = (rel_location[0] , rel_location[1] + 1)

        elif rel_location[1] == map_size[1] - 1:

            if rel_location[0] == 0:
                rel_location = (rel_location[0],rel_location[1]-1)
            else:
                rel_location = (rel_location[0] -1 , rel_location[1])

        elif rel_location[0] == 0:

            if rel_location[1] == 0:
                rel_location = (rel_location[0] + 1, rel_location[1])

            else:
                rel_location = (rel_location[0],rel_location[1] - 1)

    return destroyed
def main():
    '''Main output code'''

##    print(reader()) #- Working as intended

    initial_data = reader()
    map_size = initial_data[-1]
    asteroids = initial_data[0]

    results = []
    print('asteroid list is %s' % (str(asteroids)))
    sorted = asteroids[:].sort()
    print('sorted list is %s' % (str(sorted)))

    for asteroid in asteroids:

        checker = check_asteroid(asteroid,asteroids,map_size)
        results.append(len(checker))

##    print('final output: %s' % (check_asteroid((4,0),asteroids,map_size))) #- Working as intended

##    print(raytrace( (5,5),(0,0) )) #- Working as intended

    copy = results[:]
    copy.sort()
    max = copy[-1]
    index = results.index(max)
    ast = asteroids[index]

    print('asteroid is %s' % (str(ast)))
    
    return vaporize(ast,asteroids,map_size)

print(main())
