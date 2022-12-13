#!/usr/bin/python
import string
# Advent of code 2022 challenge 2
import string as st
import functools

file = open('input', 'r')

cur_string = ''
marker_pos = 1

with file as f:
    for line in f:
        for char in line:
            cur_string = cur_string+char
            if len(cur_string) > 4:
                cur_string = cur_string[-4:]
            print(cur_string)
            if len(set(cur_string)) == len(cur_string) & len(cur_string) == 4:
                print("Start of Packet Marker at", marker_pos)
                break
            else:
                marker_pos += 1

