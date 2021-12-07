!/usr/bin/python

# Advent of code 2021 challenge 5

file = open('input', 'r')
with file as f:
    draws = f.readline().strip()
    draws = draws.split(',')
    i = 0
    while i < len(draws):
        draws[i] = int(draws[i])
        i += 1

print(draws)
