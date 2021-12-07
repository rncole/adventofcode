#!/usr/bin/python

# Advent of code 2021 challenge 6

file = open('input', 'r')
#file = open('sample', 'r')
i = 0
with file as f:
    lanternfish = f.readline().strip()
    lanternfish = lanternfish.split(',')
    while i < len(lanternfish):
        lanternfish[i] = int(lanternfish[i])
        i += 1

j = 0
days = 0
lanternfish_temp = []
while days < 80:
    days += 1
    while j < len(lanternfish):
        if lanternfish[j] == 0:
            lanternfish[j] = 6
            lanternfish_temp.append(8)
        else:
            lanternfish[j] = lanternfish[j] - 1
        j += 1
    lanternfish.extend(lanternfish_temp)
    lanternfish_temp = []
    j = 0
    print("Processing day", days)
    #print(lanternfish)
print("The number of lanternfish after", days, "days is", len(lanternfish))
