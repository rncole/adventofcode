#!/usr/bin/python


# Advent of code 2021 challenge 1
import string as st
import functools

file = open('input', 'r')

line = 0
prev_line = 0
depth_count_larger = 0

# Solution Part 1:
with file as f:
    for line in f:
        line = int(line)
        if prev_line == 0:
            prev_line = line
        if line > prev_line:
            depth_count_larger += 1
        prev_line = line

print("Depth Count Larger than Previous: ", depth_count_larger)

# Solution part 2:
file = open('input', 'r')
list_a = []
list_b = []
list_c = []
list_d = []
n_a = 0
n_b = 1
n_c = 2
n_d = 3
sum_list = [0, 0]
sum_list_larger = 0

with file as f:
    for line in f:
        if n_a == 3:
            list_a = []
            n_a = 0
        else:
            list_a.append(int(line))
            n_a += 1
        if len(list_a) == 3:
            sum_a = list_a[0] + list_a[1] + list_a[2]
            sum_list.append(sum_a)
            del sum_list[0]
            if sum_list[1] > sum_list[0] and sum_list[0] > 0:
                sum_list_larger += 1


        if n_b == 3:
            list_b = []
            n_b = 0
        else:
            list_b.append(int(line))
            n_b += 1
        if len(list_b) == 3:
            sum_b = list_b[0] + list_b[1] + list_b[2]
            sum_list.append(sum_b)
            del sum_list[0]
            if sum_list[1] > sum_list[0] and sum_list[0] > 0:
                sum_list_larger += 1

        if n_c == 3:
            list_c = []
            n_c = 0
        else:
            list_c.append(int(line))
            n_c += 1
        if len(list_c) == 3:
            sum_c = list_c[0] + list_c[1] + list_c[2]
            sum_list.append(sum_c)
            del sum_list[0]
            if sum_list[1] > sum_list[0] and sum_list[0] > 0:
                sum_list_larger += 1

        if n_d == 3:
            list_d = []
            n_d = 0
        else:
            list_d.append(int(line))
            n_d += 1
        if len(list_d) == 3:
            sum_d = list_d[0] + list_d[1] + list_d[2]
            sum_list.append(sum_d)
            del sum_list[0]
            if sum_list[1] > sum_list[0] and sum_list[0] > 0:
                sum_list_larger += 1

print("3-Element Larger than Previous: ", sum_list_larger)








