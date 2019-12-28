#! python3

# Advent of Code Day 3 Part 1

import matplotlib.pyplot as plt

#TODO: Write the function that plots the path

plt.ylabel('Up-down')
plt.xlabel('Left-Right')

def plotPath(path):

    assert type(path) == str

    pathList = path.split(',')
    
##    print(pathList) - Working as intended
    xVal = [0]
    yVal = [0]

    for line in pathList:

        if line[0] == 'R':
            xVal.append(xVal[-1]+int(line[1:]))
            yVal.append(yVal[-1])
##            pass

        elif line[0] == 'L':
            xVal.append(xVal[-1]-int(line[1:]))
            yVal.append(yVal[-1])
##            pass
        
        elif line[0] == 'U':
            xVal.append(xVal[-1])
            yVal.append(yVal[-1]+int(line[1:]))
##            pass

        elif line[0] == 'D':
            xVal.append(xVal[-1])
            yVal.append(yVal[-1]-int(line[1:]))
##            pass

        else:
            print('Invalid Path')
            assert False #For error handling

##        print('%s,%s' % (xVal,yVal)) - Working as intended

    plt.plot(xVal,yVal)

##    plt.show() - Working as intended

##plotPath('R8,U5,L5,D3')

#TODO: Graph up both wire paths

file = open('aoc3.txt','r')
raw_input = file.readlines()
inputs = [raw_input[0][:-1],raw_input[1]]
##print(inputs) - Working as intended

for i in inputs:

    plotPath(i)

plt.show() #- Working as intended

#TODO: Write a command that finds all intersections

#intersects -

##(-7339,3077) - 10416
##(-693,1740) - 2430 : Too high
##(-2185,8) - 2193 : Correct
##(-1860,629) - 2489

##def findIntersect():
##
##    

#TODO: Find the closest intersection based on the Manhattan Distance

#TODO: Return the value
