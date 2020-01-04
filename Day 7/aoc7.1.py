#! python3

#Advent of Code Day 7

import intcode as ic

#ACS - Amplifier Controller Software
acs_input = ic.readfile('aoc7.txt')

def amp_simulation(phase_setting,input_signal):

    acs_copy = acs_input[:]
    program = ic.intcode(acs_copy)
    
        

