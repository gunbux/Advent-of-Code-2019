#! python3

# AOC 1 - Advent of Code Problem 1

#TODO: Save input as variable

import os
import math

file = open('aoc1.txt','r')
modules = file.readlines()
###Debuggin statement
##for i in modules:
##    print(i)

total_fuel = 0

def fuel_calc(number):

    return math.floor((float(number)/3))-2

for mod in modules:

    remaining_fuel = int(mod)
    #Debug statements
##    print('Current module/fuel: %s' % (remaining_fuel))
    while remaining_fuel > 0 :
        if fuel_calc(remaining_fuel) > 0:
            total_fuel += fuel_calc(remaining_fuel)
##        print('Total fuel at: %s' % (total_fuel))
        remaining_fuel = fuel_calc(remaining_fuel)
##        print('Remaining fuel: %s' % (remaining_fuel))

###TODO: Input the formula to find how much fuel is needed
##
##for mod in modules:
##
##    #Debugging statements
##    print('Current module: %s' % (mod))
##    calculation = int(mod)
##    print('first calc: %s: ' %(str(calculation)))
##    calculation = float(calculation)/3
##    print('second calc: %s: ' %(str(calculation)))
##    calculation = math.floor(calculation)
##    print('third calc: %s: ' %(str(calculation)))
##    calculation -= 2
##    print('fourth calc: %s: ' %(str(calculation)))
##    total_fuel += calculation
####    total_fuel += round((int(mod)/3)-0.5)-2
##    print('Current total fuel at %s' % (total_fuel))
##
###TODO: Find total fuel needed and send output
##
##
print('Total fuel required: %s' % (total_fuel))
file.close()
