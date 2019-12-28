#! python3

# Advent of Code Day 16

# Convuluted piece of shit

#Step 3: Run phase

def offset(input):

    return input[1:]

def update(input,pattern):

    sum = 0

    for step in range(len(input)):
        sum += int(input[step]) * pattern[step]

##    print(f'Sum is {sum}') #- Working as intended
    sum = str(abs(sum))
##    print(f'Returning value: {sum[-1]}') #- Working as intended

    return sum[-1]

def runPhase(input):

    #Step 1: Get length of input

    input_length = len(input)
    patternList = getPattern(input_length)
    new_input = ''

    for pattern in patternList:
        new_input += update(input,pattern)

##    print(f'Phase Complete. New input is {new_input}') #- Working as intended
    return new_input

#Step 2 : Get repeating pattern

def getPattern(inpLength):

    patternList = []
    base = [0,1,0,-1]

    for step in range(inpLength):

        pattern = []
        while len(pattern) < inpLength + 1:
            for m in base:
                for i in range(step+1):
                    pattern.append(base[m])

##        print(f'Pattern for step {step + 1} is {pattern} (Without offset)') #- Working as intended

        pattern = offset(pattern[:len(input)+1])
        patternList.append(pattern)

##        print(f'New pattern is {pattern}') #- Working as intended
##        update(input,pattern)


    return patternList

def simulation(input,phases=100,current_phase = 1):

# Recursive solution
    if current_phase != phases:
##        print(f'Running simulation with input {input}') #- Working as intended
        new_input = runPhase(input)
        current_phase += 1

        return simulation(new_input,phases,current_phase)

    elif current_phase == phases:
##        print(f'Running simulation with input {input}') #- Working as intended
        new_input = runPhase(input)
        print(f'Simulation Complete. Final output is {new_input}')
##        ans = new_input[:8] #- Irrelevant for Part 2
##        print(f'First 8 digits of answer is {ans}') #- Irrelevant for Part 2
        return new_input

#Alternative function without recursion
##    input = initial_input
##
##    for i in range(phases):
##        print(f'Running simulation with input {input}')
##        input = runPhase(input)        
##
##    return input

#Test Cases
##simulation('12345678',4) #- Working as intended
##simulation('80871224585914546619083218645595',100) #- Working as intended
##simulation('19617804207202209144916044189917') #- Working as intended
##simulation('69317163492948606335995924319873') #- Working as intended

def readFile(filename):
    file = open(filename , 'r')
    input = file.read()
    file.close()

    return input
    
input = readFile('aoc16.txt')

for i in range(10000):
    input += input

output = simulation(input)
offset = output[:7]
final_digits = output[offset:offset+8]
