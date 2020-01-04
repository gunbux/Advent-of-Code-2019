#! python3

#Advent of Code - Intcode implementation

class opcode:

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

            if memory[pointer] == 1 :
                memory[memory[pointer+3]] = memory[memory[pointer+1]] + memory[memory[pointer+2]]
                pointer+=4
                  
            elif memory[pointer] == 2:
                memory[memory[pointer+3]] = memory[memory[pointer+1]] * memory[memory[pointer+2]]
                pointer+=4

            elif memory[pointer] == 3:
                memory[memory[pointer+1]] = input('Input a number: ')
                pointer+=2

            elif memory[pointer] == 4:
                 print(f'Output at {memory[pointer+1]} is memory[memory[pointer+1]]')
                 pointer+=2

            elif memory[pointer] == 99:
                pointer+=1
                return self.getMemory()
            
            else:
                print("FUCK")

        return self.getMemory()

    def grammar(self,noun,verb):
        self.setMemory(1,noun)
        self.setMemory(2,verb)
        return self.getMemory()

def convertolist(flist):
    stripped = flist.rstrip('\n')
    split = stripped.split(',')
    tape = [int(split[x])  for x in range(len(split))]
    return tape

def run():

    filename = input('Please input file name: ')

    file = open(filename,'r')
    memory = convertolist(file.read())

    sol = opcode(memory)
    for n in range(100):
        for v in range(100):
            sol.grammar(n,v)
            sol.run()

            if sol.getMemory()[0] == 19690720:
                print(f'Noun and verb are {sol.getMemory()[1]} and {sol.getMemory()[2]}')
            sol.resetMemory()
##    print(sol.run())
    
    pass

##run()
