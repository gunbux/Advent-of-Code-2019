with open('aoc2.txt', 'r') as inpfile:
    readfile = inpfile.read()

def convertolist(flist):
    stripped = flist.rstrip('\n')
    split = stripped.split(',')
    tape = [int(split[x])  for x in range(len(split))]
    return tape

memory = convertolist(readfile)
pointer = 0
while True :    
    
    if memory[pointer] == 1 :
        memory[memory[pointer+3]] = memory[memory[pointer+1]] + memory[memory[pointer+2]]
        pointer+=4
          
    elif memory[pointer] == 2:
        memory[memory[pointer+3]] = memory[memory[pointer+1]] * memory[memory[pointer+2]]
        pointer+=4

    elif memory[pointer] == 99:
        break
    
    else:
        print("FUCK")
        
print(memory)
