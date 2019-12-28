#! python3

# Advent of Code Day 8

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
    print('list of zero counts: %s' % (zeroList))
    print('Lowest zero count is %s' % (zeroList[0]))
    lowestVal = zeroList[0]
    index = copy.index(lowestVal)
    

    return list[index]

def countDigit(layer,digit):

    count = 0
    for i in layer:

        if i == digit:

            count += 1
    print('Total number of %s: %s' % (digit,count))
    return count

def main(width,height):
    '''Returns the output for the question'''

    file = open('aoc8.txt','r') #- Actual input
##    file = open('aoc8test.txt','r') #- Test input
    input = file.read()
    file.close

    print('Input is %s' % (input))

    layers = []
    layer_size = width * height
##    print('Pic of %s by %s. Total size is %s' % (width,height,layer_size)) #- Working as intended

    count = 0
    while count < len(input):

        count += layer_size
        layers.append(input[count - layer_size:count])
##        print('Current list of layers: %s' % (layers)) #- Working as intended


    zero_layer = countZero(layers)
    print('Number of 1s: %s' % (countDigit(zero_layer,'1')))
    print('Number of 2s: %s' % (countDigit(zero_layer,'2')))

    multiply = countDigit(zero_layer,'1') * countDigit(zero_layer,'2')

    print('Program Complete.')
    return multiply
    
    
# Test Case:

##print(main(3,2))

# Actual Case:

print(main(25,6)) #- Working as intended
