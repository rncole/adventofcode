#!/usr/bin/python

# Advent of code 2021 challenge 8
import math

file = open('input', 'r')
#file = open('sample', 'r')

input = []
unique_count = 0
i = 0
with file as f:
    input = f.readlines()

display_data_raw = []
for each in input:
    data = each.strip()
    data = data.split(' | ')
    display_data_raw.append(data)

i = 0
while i < len(display_data_raw):
    display = display_data_raw[i][1]
    display = display.split(' ')
    for j in range(0,len(display)):
        if len(display[j]) == 2 or len(display[j]) == 4 or len(display[j]) == 3 or len(display[j]) == 7:
            #print("adding 1 to count for", display[j])
            unique_count += 1
        j += 1
    i += 1
print("Segments for 1, 4, 6, and 8 appear", unique_count, "times.")