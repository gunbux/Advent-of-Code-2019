#! python3
# Advent of Code - Day 7

def getValues(pointer,memory):

    opcode = str(memory[pointer])

    if int(opcode[-2:]) in [1,2,5,6,7,8]:
        
        while len(opcode) < 5:
            opcode = '0' + opcode

        if opcode[-3] == '0':
            value1 = memory[memory[pointer+1]]
        elif opcode[-3] == '1':
            value1 = memory[pointer+1]

        if opcode[-4] == '0':
            value2 = memory[memory[pointer+2]]
        elif opcode[-4] == '1':
            value2 = memory[pointer+2]

##        print(f'Values are {value1} and {value2}')
        return value1,value2

    elif int(opcode[-2:]) == 4:

        while len(opcode) < 3:
            opcode = '0' + opcode

        if opcode[-3] == '0':
            return memory[memory[pointer+1]]
        elif opcode[-3] == '1':
            return memory[pointer+1]

    else:
        print('Error, invalid opcode')

def getopcode(value):

    opcode = str(value)
    try:
        return int(opcode[-2:])
    except:
        print('Half error')
        return int(opcode)

class intcode:

    def __init__(self,input):
        self.memory = input
        self.backup = input[:]
        pass

    def resetMemory(self):
        self.memory = self.backup[:]
        pass
    
    def getMemory(self):
        return self.memory

    def setMemory(self,position,value):
        self.memory[position] = value
        return self.memory

    def run(self):
        memory = self.memory
        pointer = 0
        while True:

##            print(f'Current memory is: {memory}')
##            print(f'Pointer location at {pointer}')
##            print(f'Value at pointer is {memory[pointer]}')
##            print(f'Next 3 values are {memory[pointer+1],memory[pointer+2],memory[pointer+3]}')

            if getopcode(memory[pointer]) == 1:
                values = getValues(pointer,memory)
##                print(f'Values are {values}') #- Working as intended
                memory[memory[pointer+3]] = values[0] + values[1]
                pointer+=4

            elif getopcode(memory[pointer]) == 2:
                values = getValues(pointer,memory)
                memory[memory[pointer+3]] = values[0] * values[1]
                pointer+=4

            elif getopcode(memory[pointer]) == 4:
                value = getValues(pointer,memory)
                print(f'Value output is {value}')
                pointer+=2

            elif getopcode(memory[pointer]) == 5:
                values = getValues(pointer,memory)
                if values[0] != 0:
##                    print(f'Jumping to position: {values[1]}')
                    pointer = values[1]
                else:
                    pointer+=3

            elif getopcode(memory[pointer]) == 6:
                values = getValues(pointer,memory)
                if values[0] == 0:
##                    print(f'Jumping to position: {values[1]}')
                    pointer = values[1]
                else:
                    pointer+=3

            elif getopcode(memory[pointer]) == 7:
                values = getValues(pointer,memory)
                if values[0] < values[1]:
                    memory[memory[pointer+3]] = 1

                else:
                    memory[memory[pointer+3]] = 0
                pointer+=4

            elif getopcode(memory[pointer]) == 8:
                values = getValues(pointer,memory)
                if values[0] == values[1]:
                    memory[memory[pointer+3]] = 1

                else:
                    memory[memory[pointer+3]] = 0
                pointer+=4
                    
            elif memory[pointer] == 3:
                memory[memory[pointer+1]] = int(input('Input a number: '))
                pointer+=2

            elif memory[pointer] == 99:
                pointer+=1
                print('Program terminated')
                return self.getMemory()
            
            else:
                print("FUCK")
                print(memory)
                break

            


## DAY 2 IMPLEMENTATION BELOW FOR REFERENCE
##            if memory[pointer] == 1 :
##                memory[memory[pointer+3]] = memory[memory[pointer+1]] + memory[memory[pointer+2]]
##                pointer+=4
##                  
##            elif memory[pointer] == 2:
##                memory[memory[pointer+3]] = memory[memory[pointer+1]] * memory[memory[pointer+2]]
##                pointer+=4
##
##            elif memory[pointer] == 3:
##                memory[memory[pointer+1]] = input('Input a number: ')
##                pointer+=2
##
##            elif memory[pointer] == 4:
##                 print(f'Output at {memory[pointer+1]} is memory[memory[pointer+1]]')
##                 pointer+=2
##
##            elif memory[pointer] == 99:
##                pointer+=1
##                return self.getMemory()
##            
##            else:
##                print("FUCK")
##
##        return self.getMemory()

    def grammar(self,noun,verb):
        self.setMemory(1,noun)
        self.setMemory(2,verb)
        return self.getMemory()

def convertolist(flist):
    stripped = flist.rstrip('\n')
    split = stripped.split(',')
    tape = [int(split[x])  for x in range(len(split))]
    return tape

def readfile(filename):

    file = open(filename,'r')
    return converttolist(file.read)
##def run():
##
##    filename = 'aoc7.txt'
##
##    file = open(filename,'r')
##    memory = convertolist(file.read())
##
##    sol = opcode(memory)
##    sol.run()
####    print(sol.run())
##    
##    pass
##
##run()
