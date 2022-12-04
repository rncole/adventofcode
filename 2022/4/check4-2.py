#!/usr/bin/python
import string
# Advent of code 2022 challenge 2
import string as st
import functools

file = open('input', 'r')

priority_sum = 0
assignments_overlap = 0

with file as f:
    for line in f:
        assignment_1 = line.partition(',')[0].strip()
        assignment_2 = line.partition(',')[2].strip()
        assignment_1_start = int(assignment_1.partition('-')[0])
        assignment_1_end = int(assignment_1.partition('-')[2])
        assignment_2_start = int(assignment_2.partition('-')[0])
        assignment_2_end = int(assignment_2.partition('-')[2])
        assignment_1_list = list(range(assignment_1_start, assignment_1_end+1))
        assignment_2_list = list(range(assignment_2_start, assignment_2_end+1))
        if any(elem in assignment_1_list for elem in assignment_2_list):
            assignments_overlap += 1
        elif any(elem in assignment_2_list for elem in assignment_1_list):
            assignments_overlap += 1

print("There are", assignments_overlap, "pairs that overlap.")
