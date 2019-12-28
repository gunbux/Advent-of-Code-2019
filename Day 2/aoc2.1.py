#! python3

#Advent of Code Day 2 Part 1

#TODO: Get input from file

import os

file = open('aoc2.txt','r')

input = file.read()
initialList = input.split(',') #Splits the text file into respective int elements, using the , as the divided. However ints are saved as string so remember to convert them
inputList = []
opCount = 0
operationComplete = False

for i in initialList:
    inputList.append(int(i))

print('Input List is: %s' % (inputList))

#Converts all the strings in initialList to an int and stores them in a new list, inputList.

operationList = []
##outputList = inputList[:]

#TODO: Execute opcodes via functions/classes

def opcode(list):
    #opcode operation for a single list of length 4.

    global inputList
    global operationComplete

##    print('Current operation on list: %s' % (list))

    id = list[0]

    if id == 1:
        #Opcode 1 - Addition
        
        returnValue = inputList[list[1]] + inputList[list[2]]
        position = list[3]

##        list.remove(position)
##        list.insert(position,sum)

    elif id == 2:
        #Opcode 2 - Multiplication

        returnValue = inputList[list[1]] * inputList[list[2]]
        position = list[3]


    elif id == 99:
        #Opcode 99 - Halt program
        print('Halting program...')
        operationComplete = True
        return inputList

    else:
##        print('Invalid ID detected')
        pass
        

    inputList.pop(position)
    inputList.insert(position,returnValue)

##    print('New input list is now: %s' % (inputList))
    return inputList

#TODO: Opcode operation for continuous input

def operation(inputList):

    global operationList
##    global outputList
    global opCount

    while operationComplete == False:

        if opCount == 0:
            for i in range(4):
                operationList.append(inputList[i])
                opCount += 1

        else:
            for i in range(opCount,opCount+4):
                operationList.append(inputList[i])
                opCount += 1

        opcode(operationList)
        operationList.clear()

    print('Operation complete.')
    return inputList

#TODO: Return final output back

print(operation(inputList))
