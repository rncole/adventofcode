#!/usr/bin/python


# Advent of code 2022 challenge 1
import string as st
import functools

file = open('input', 'r')

line = 0
elf_num = 0
calories = [0]

with file as f:
    for line in f:
        if(line == '\n'):
            elf_num += 1
            calories.append(0)
        else:
            item_cal = int(line)
            calories[elf_num] += item_cal

elf_num_max_calories = calories.index(max(calories))
elf_calories = max(calories)
sorted_calories = sorted(calories,reverse=True)[:3]

print("Elf",elf_num_max_calories,"has the most calories with",elf_calories)
print("The top 3 Elves are carrying",sum(sorted_calories),"calories")