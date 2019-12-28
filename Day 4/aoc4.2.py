#! python3

# Advent of Code Day 4 Part 1

#TODO: Modularity: Create functions for each of the requirements for the password

def isSixDigit(input):

    if len(input) == 6 and type(input) == str:

        return True

    else:

##        print('Digit Error found')
        return False

##def isAdjacent(input): # - Irrelevant for part 2
##
##    for i in range(len(input)-1):
##
##        if input[i] == input[i+1]:
##
####            try:
####                if input[i+1] == input[i+2]:
####
####                    continue
####    
####            except IndexError:
####
####                return True
##
##            return True
##
####    print('Found not adjacent')
##    return False

#Failed attempts
####def recursiveAdjacent(input,integer,count,maxCount):
####
####    currentCount = count
####
#####Updates maxCount
####    
####    if currentCount > maxCount:
####
####        maxCount = currentCount
####
#####Recursive element
####        
####    if len(input) == 0:
####
####        print('maxCount =: %s' % (maxCount))
####
####        return maxCount
####
####    elif input[0] == integer:
####
####        return recursiveAdjacent(input[1:],integer,currentCount+1,maxCount)
####
####    else:
####
####        return recursiveAdjacent(input[1:],integer,0,maxCount)

        
#Test inputs

##recursiveAdjacent('110',1,0,0) #- Should output 2
##recursiveAdjacent('110111',1,0,0) #- Should output 3
##recursiveAdjacent('909099',9,0,0) #- Should output 2
        
def checkAdjacent(input,position):

    adjCount = 0

    if position == 0:

        if input[0] == input[1]:

            adjCount += 1

    elif position == len(input) - 1:

        if input[len(input) - 1 ] == input[len(input) - 2 ]:

            adjCount += 1

    else:

        if input[position] == input[position - 1]:

            adjCount += 1

        if input[position] == input[position + 1]:

            adjCount += 1


##    print('Final adjCount is: %s' % (adjCount)) #- Working as intended
    return adjCount

###Test inputs for checkAdjacent()
##
##checkAdjacent('11234',0)
##checkAdjacent('123444',4)

def isAdjacent(input):

    for i in range(len(input)-1):

        if checkAdjacent(input,i) == 1 and checkAdjacent(input,i+1) == 1 and input[i] == input[i+1]:

            return True

    return False
##def isSuperAdjacent(input):
##
##    for i in range(len(input)):
##
##        if input[i] == input[i+1] and input[i+1] == input[i+2]:
##
##            return True
##
##    return False

def isIncreasing(input):

##    print('Input is: %s' % (input))

    for i in range(len(input)-1):

##        print('Checking %s with %s' % (input[i],input[i+1]))

        if int(input[i]) > int(input[i+1]):

##            print('Returning False')
            return False

##    print('Not in increasing order')
##    print('Returning True')
    return True

#TODO: Grab input and iterate through all numbers for possible password

def main():

    inp = input('Enter puzzle input range (e.g 1-100): ')
    ranger = inp.split('-')

    numCount = 0
    range_int = []
    for i in ranger:
        range_int.append(int(i))

##    print(range_int) # - Working as intended

    for i in range(range_int[0],range_int[1]):

        i = str(i)
        if isSixDigit(i) and isAdjacent(i) and isIncreasing(i):
##            print('Number found: %s' % (i)) #- Working as intended
            numCount += 1

    return numCount

#TODO: Return total number of possible passwords

print(main())
