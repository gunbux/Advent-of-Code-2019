#! python3

# Advent of Code Day 2 Part 2

from aoc2 import operation

file = open('aoc2.txt','r')

input = file.read()
initialList = input.split(',') #Splits the text file into respective int elements, using the , as the divided. However ints are saved as string so remember to convert them
inputList = []
tempList = []

for i in initialList:
    inputList.append(int(i))

file.close()


for noun in range(100):
    
    tempList = inputList[:]
    
    tempList.pop(1)
    tempList.insert(1,noun)
    print('Current noun is: %s' % (noun))
    for verb in range(100):

        tempList.pop(2)
        tempList.insert(2,verb)
        opList = tempList[:]
##        print('Current verb is: %s' % (verb))
##        print('Current input list is: %s' % (opList))
        operation(opList)
##        print('Output list is %s' % (opList))
##        print('Current value at %s' % (opList[0]))

        if opList[0] == 19690720:
            print('Solotion found: Noun is %s, and verb is %s.' % (noun,verb))
            print('Ideal output is %s' % (100 * noun + verb))
            break
        

        
        


    

    

    

        
