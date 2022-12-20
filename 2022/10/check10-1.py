#!/usr/bin/python
import string
# Advent of code 2022 challenge 2
import string as st
import functools
import numpy as np

file = open('input', 'r')
cycle_count = 1
reg_X = 1
reg_V = 0
reg_V_stack_1 = 0
signal_sum = 0

with file as f:
    for line in f:
        if line[:4] == "noop":
            reg_V = reg_V_stack_1
            reg_V_stack_1 = 0
        if line[:4] == "addx":
            cycle_count += 1
            reg_V_stack_1 = int(line[5:].strip("\n"))
        reg_V = reg_V_stack_1
        if line[:4] == "addx" and cycle_count in (20, 60, 100, 140, 180, 220):
            print("Cycle:", cycle_count, "\n Register:", reg_X, "\n reg_V:", reg_V, "\n reg_V_stack_1:", reg_V_stack_1,
                  "Signal:", cycle_count * reg_X)
            signal_sum += (cycle_count * reg_X)
            print("Sum of Signals:", signal_sum)
        reg_X += reg_V
        cycle_count += 1
        if cycle_count in (20, 60, 100, 140, 180, 220):
            print("Cycle:", cycle_count, "\n Register:", reg_X, "\n reg_V:", reg_V, "\n reg_V_stack_1:", reg_V_stack_1,
                  "Signal:", cycle_count * reg_X)
            signal_sum += (cycle_count * reg_X)
            print("Sum of Signals:", signal_sum)

