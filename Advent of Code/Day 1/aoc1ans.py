import os


file = open('aoc1.txt','r')

ans = sum([(int(x) // 3) - 2for x in file.read().split('\n')])

print(ans)
