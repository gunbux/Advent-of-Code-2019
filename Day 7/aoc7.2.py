#! python3

#Advent of Code Day 7

import intcode as ic

#ACS - Amplifier Controller Software
##acs_input = ic.readfile('aoc7.txt')

#Test Inputs
acs_input = ic.readfile('test4.txt')
##acs_input = ic.readfile('test5.txt')

def amp_simulation(phase_setting,input_signal,acs = None,first_input = True):

    if acs == None:
        acs_copy = acs_input[:]
    else:
        acs_copy = acs[:]
    program = ic.intcode(acs_copy)

    if first_input == True:
        return program.run([phase_setting,input_signal])
    else:
        return program.run([input_signal])
    
def simulation(phase_settings,acs_list = None):

    input_signal = 0

    if acs_list == None:
        acs_list = [acs_input[:],acs_input[:],acs_input[:],acs_input[:],acs_input[:]]

    halted = False
    first_input = True

    while halted == False:
        for amp in range(5):
    ##        print(f'Current signal is: {input_signal}') # Working as intended
            output = amp_simulation(phase_settings[amp],input_signal,acs_list[amp],first_input)
            input_signal = output[0]
            acs_list[amp] = output[1]
            halted = output[2]

            print(f'Current input signal is {input_signal}')

        first_input = False

##    print(f'Final signal strength is: {input_signal}') # Working as intended
    return input_signal

def multiplecounts(list):

    if [list.count(5),list.count(6),list.count(7),list.count(8),list.count(9)] == [1,1,1,1,1]:
        return False

    else:
        return True
    
def run():

    ans = 0
    best = None
    permutations = []
    num = 0
    for i in range(5,10):
        for m in range(5,10):
            for n in range(5,10):
                for k in range(5,10):
                    for j in range(5,10):
                        permutations.append([i,m,n,k,j])

    for permutation in permutations:

        if multiplecounts(permutation):
##            print('Multiple counts detected, skipping...')
            continue
        
        num+=1
        result = simulation(permutation)
        if result > ans:
            ans = result
            best = permutation

    print(f'Mote Carlo simulation complete. Number of simulations: {num}. Final output is {ans} using the order {best}')
    return ans,best

print(run())
