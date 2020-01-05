#! python3

#Advent of Code Day 7

import intcode as ic

#ACS - Amplifier Controller Software
acs_input = ic.readfile('aoc7.txt')

#Test Inputs
##acs_input = ic.readfile('test1.txt')
##acs_input = ic.readfile('test2.txt')
##acs_input = ic.readfile('test3.txt')

def amp_simulation(phase_setting,input_signal,acs = None):

    if acs == None:
        acs_copy = acs_input[:]
    else:
        acs_copy = acs[:]
    program = ic.intcode(acs_copy)
    return program.run([phase_setting,input_signal])
    
def simulation(phase_settings):

    input_signal = 0

    for amp in range(5):
##        print(f'Current signal is: {input_signal}') # Working as intended
        input_signal = amp_simulation(phase_settings[amp],input_signal)

##    print(f'Final signal strength is: {input_signal}') # Working as intended
    return input_signal

def multiplecounts(list):

    if [list.count(0),list.count(1),list.count(2),list.count(3),list.count(4)] == [1,1,1,1,1]:
        return False

    else:
        return True
    
def run():

    ans = 0
    best = None
    permutations = []
    num = 0
    for i in range(5):
        for m in range(5):
            for n in range(5):
                for k in range(5):
                    for j in range(5):
                        permutations.append([i,m,n,k,j])

    for permutation in permutations:

        if multiplecounts(permutation):
##            print('Multiple counts detected, skipping...')
            continue
        
        num+=1
        result = simulation(permutation)
        print('Sim complete')
        if result > ans:
            ans = result
            best = permutation

    print(f'Mote Carlo simulation complete. Number of simulations: {num}. Final output is {ans} using the order {best}')
    return ans,best

print(run())
