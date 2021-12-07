#!/usr/bin/python

# Advent of code 2021 challenge 6

file = open('input', 'r')
#file = open('sample', 'r')
i = 0
lanternfish_smart = {}
with file as f:
    lanternfish = f.readline().strip()
    lanternfish = lanternfish.split(',')
    while i < len(lanternfish):
        lanternfish[i] = int(lanternfish[i])
        i += 1

i = 0
while i < len(lanternfish):
    value = lanternfish[i]
    if value in lanternfish_smart:
        lanternfish_smart[value] += 1
    else:
        lanternfish_smart[value] = 1
    i += 1
#print(sum(lanternfish_smart.values()))
lanternfish_smart = dict(sorted(lanternfish_smart.items()))
#print(lanternfish_smart)

days = 0
j = 0
lanternfish_smart_temp = {}
while days < 256:
    lanternfish_smart = dict(sorted(lanternfish_smart.items()))
    #print("Day:", days, ":", lanternfish_smart)
    for j in sorted(lanternfish_smart):
        if j == 0:
            lanternfish_smart_temp[6] = lanternfish_smart.get(0)
            lanternfish_smart_temp[8] = lanternfish_smart.get(0)
        else:
            lanternfish_smart[j-1] = lanternfish_smart.get(j)
            lanternfish_smart[j] = 0

    if 6 in lanternfish_smart_temp:
        if 6 in lanternfish_smart:
            lanternfish_smart[6] += lanternfish_smart_temp.get(6)
        else:
            lanternfish_smart[6] = lanternfish_smart_temp.get(6)

    if 8 in lanternfish_smart_temp:
        if 8 in lanternfish_smart:
            lanternfish_smart[8] += lanternfish_smart_temp.get(8)
        else:
            lanternfish_smart[8] = lanternfish_smart_temp.get(8)
    lanternfish_smart_temp = {}
    days += 1
print("The number of lanternfish after", days, "days is" , sum(lanternfish_smart.values()))
