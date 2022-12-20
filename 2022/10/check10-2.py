#!/usr/bin/python
import string
# Advent of code 2022 challenge 2
import string as st
import functools
import numpy as np

file = open('input', 'r')
cycle_count = 0
reg_X = 1
reg_V = 0
reg_V_stack_1 = 0
signal_sum = 0
screen = ""

with file as f:
    for line in f:
        if line[:4] == "noop":
            reg_V = reg_V_stack_1
            reg_V_stack_1 = 0
        if line[:4] == "addx":
            cycle_count += 1
            reg_V_stack_1 = int(line[5:].strip("\n"))
        reg_V = reg_V_stack_1

        if line[:4] == "addx":
            #print(cycle_count, reg_X)
            if reg_X in range(cycle_count-1, cycle_count+2):
                screen = screen + "#"
            else:
                screen = screen + "."
            if cycle_count == 40:
                #print("40!")
                screen += "\n"
                cycle_count = 0

        reg_X += reg_V
        cycle_count += 1

        if line[:4] == "noop" or line[:4] == "addx":
            #print(cycle_count, reg_X)
            if reg_X in range(cycle_count-1, cycle_count+2):
                screen = screen + "#"
            else:
                screen = screen + "."
            if cycle_count == 40:
                #print("40!")
                screen += "\n"
                cycle_count = 0
    print(screen)
