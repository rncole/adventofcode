#!/usr/bin/python


# Advent of code 2021 challenge 2
import string as st
import functools

file = open('input', 'r')

# Position in x (horizontal), aim, z (depth) starting at 0,0:
pos = [0, 0, 0]


with file as f:
    for line in f:
        pos_dir = line.partition(' ')[0]
        pos_mag = line.partition(' ')[2]
        pos_mag = int(pos_mag)

        if pos_dir == "forward":
            aim = pos[1]
            pos = [a + b for a, b in zip(pos, [pos_mag, 0, pos_mag*aim])]
        elif pos_dir == "up":
            pos = [a - b for a, b in zip(pos, [0, pos_mag, 0])]
        elif pos_dir == "down":
            pos = [a + b for a, b in zip(pos, [0, pos_mag, 0])]

print("Final Position: ", pos)
print("Solution: ", pos[0]*pos[2])

