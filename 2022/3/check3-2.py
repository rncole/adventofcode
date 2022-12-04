#!/usr/bin/python
import string
# Advent of code 2022 challenge 2
import string as st
import functools

file = open('input', 'r')

priority_sum = 0
group_num = 1
elf_num = 1
elf_group = []

with file as f:
    for line in f:
        elf_group.append([group_num, elf_num, line.strip()])
        elf_num += 1
        if elf_num > 3:
            elf_num = 1
            group_num += 1

max_group = max(elf_group, key=lambda sublist: sublist[0])[0]

for i in range(1, max_group+1):
    for j in range(1, 4):
        elves_rucksacks = [sublist for sublist in elf_group if sublist[0] == i and sublist[1] == j]
        print(elves_rucksacks)
        if j == 1:
            elf_1_ruck = elves_rucksacks[0][2]
        if j == 2:
            elf_2_ruck = elves_rucksacks[0][2]
        if j == 3:
            elf_3_ruck = elves_rucksacks[0][2]
        j += 1
    #print(elf_1_ruck, elf_2_ruck, elf_3_ruck)

    common_item = set(elf_1_ruck) & set(elf_2_ruck) & set(elf_3_ruck)
    common_item = next(iter(common_item))
    if common_item.islower():
        item_priority = string.ascii_lowercase.index(common_item) + 1
    elif common_item.isupper():
        item_priority = string.ascii_uppercase.index(common_item) + 27
    else:
        print("No common Item or other issue in item:", common_item)
    print("Group Badge:", common_item, "\n  Priority:", item_priority)
    priority_sum += item_priority

    i += 1
    j = 1

print("Sum of Priorities is:", priority_sum)