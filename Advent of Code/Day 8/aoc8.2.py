#! python3

# Advent of Code Day 8

import turtle

def countZero(list):

    zeroList = []

    for i in list:

        zeroCount = 0
        
        for m in i:

            if m == '0':
                zeroCount += 1

        zeroList.append(zeroCount)

    copy = zeroList[:]
    zeroList.sort()
##    print('list of zero counts: %s' % (zeroList))
##    print('Lowest zero count is %s' % (zeroList[0]))
    lowestVal = zeroList[0]
    index = copy.index(lowestVal)
    

    return list[index]

def countDigit(layer,digit):

    count = 0
    for i in layer:

        if i == digit:

            count += 1
##    print('Total number of %s: %s' % (digit,count))
    return count

def draw(layer,width,height):

    print('Layer: %s' % (layer))

    turtle.pu()
    turtle.screensize(3,1)
    index = 0

    for i in range(height):

        for m in range(width):
            
##            print('Turtle Position is at: %s,%s' % (m,i))
            turtle.setpos(int(m)*10,int(-i)*10)
            
            if layer[index] == '0':
##                turtle.pen(pencolor='black')
##                turtle.pd()
##                turtle.pu()
##                print('dotting black')
                turtle.dot(10,'orange')

            elif layer[index] == '1':
##                turtle.pen(pencolor='white')
##                turtle.pd()
##                turtle.pu()
##                print('dotting white')
                turtle.dot(10,'red')

            else:
                pass

##            print(index)

            index += 1
##        index += 1
    pass

##def draw(list):
##
##    list.reverse()
##
##    turtle.pu()
##    turtle.screensize(25,6)
##    print('Current screensize: %s' % (str(turtle.screensize())))
##    for i in range(len(list)):
##
##        for m in range(len(list[i])):
##
##            print('Turtle Position is at: %s,%s' % (m,i))
##            turtle.setpos(int(m),int(i))
##            if list[i][m] == '0':
####                turtle.pen(pencolor='black')
####                turtle.pd()
####                turtle.pu()
##                print('dotting black')
##                turtle.dot(2,'black')
##
##            elif list[i][m] == '1':
####                turtle.pen(pencolor='white')
####                turtle.pd()
####                turtle.pu()
##                print('dotting white')
##                turtle.dot(2,'grey')
##
##            else:
##                pass

def main(width,height):
    '''Returns the output for the question'''

    file = open('aoc8.txt','r') #- Actual input
##    file = open('aoc8test.txt','r') #- Test input
    input = file.read()
    file.close

##    print('Input is %s' % (input))

    layers = []
    layer_size = width * height
    layer_count = 0
##    print('Pic of %s by %s. Total size is %s' % (width,height,layer_size)) #- Working as intended

    count = 0
    while count < len(input):

        count += layer_size
        layers.append(input[count - layer_size:count])
##        print('Current list of layers: %s' % (layers)) #- Working as intended


    zero_layer = countZero(layers)
##    print('Number of 1s: %s' % (countDigit(zero_layer,'1')))
##    print('Number of 2s: %s' % (countDigit(zero_layer,'2')))

    multiply = countDigit(zero_layer,'1') * countDigit(zero_layer,'2')

    print('First layer should be %s' % (layers[-1]))

    layers.reverse()

    print('Layer check %s' % (layers[0]))
    

    for layer in layers:
        layer_count += 1
        draw(layer,width,height)
        print('Currently at: Layer %s' % (layer_count))


    print('Program Complete.')
    return multiply
    
    
# Test Case:

##print(main(3,2))

# Actual Case:

print(main(25,6)) #- Working as intended
