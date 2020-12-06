#!/usr/bin/python


# Advent of code challenge 3
import string as st

file = open('input', 'r')

i = 0
j = 0
tf = 0
tc = 0


#len = sum(1 for line in file)*31
len = 11000
#print len
tree = "#"

while i < len:
    file.seek(i,0)
    line = file.readline()
    tf =  line.find('#', j)
    if tf == j:
        tc += 1
#    print i
#    print j
    if j <= 25:
        j += 5
    else:
        if j == 26:
            j = 0
        if j == 27:
            j = 1
        if j == 28:
            j = 2
        if j == 29:
            j = 3
        if j == 30:
            j = 4
#    print(line)
    i += 32

print "Trees Found: ",tc

