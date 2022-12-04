#!/usr/bin/python
import string
# Advent of code 2022 challenge 2
import string as st
import functools

file = open('input', 'r')

priority_sum = 0

with file as f:
    for line in f:
        line_length = len(line.strip())
        half_length = int(line_length/2)
        compartment_1, compartment_2 = line[:half_length], line[half_length:]
        # print("Compartment 1:", compartment_1)
        # print("Compartment 2:", compartment_2)
        common_item = ''.join(set(compartment_1).intersection(compartment_2))
        if common_item.islower():
            item_priority = string.ascii_lowercase.index(common_item) + 1
        elif common_item.isupper():
            item_priority = string.ascii_uppercase.index(common_item) + 27
        else:
            print("No common Item or other issue in item:", common_item)
        print("Item in Both Compartments:", common_item, "\n  Priority:",item_priority)
        priority_sum += item_priority

print("Sum of Priorities is:", priority_sum)