#!/usr/bin/python

# Advent of code 2021 challenge 6
import math

file = open('input', 'r')
#file = open('sample', 'r')
i = 0
with file as f:
    crab_list = f.readline().strip()
    crab_list = crab_list.split(',')
    while i < len(crab_list):
        crab_list[i] = int(crab_list[i])
        i += 1
i = 0
crab_distribution = {}
while i < len(crab_list):
    value = crab_list[i]
    if value in crab_distribution:
        crab_distribution[value] += 1
    else:
        crab_distribution[value] = 1
    i += 1
crab_distribution = dict(sorted(crab_distribution.items()))

sum_crabs = sum(crab_list)

fuel_cost = {}
for i in range(min(crab_distribution), max(crab_distribution)):
    fuel_cost[i] = 0
    i += 1

for i in fuel_cost:
    fuel_cost[i] = 0
    for j in crab_distribution:
        fuel_expended = ((((abs(j - i) ** 2) + abs(j - i)) / 2) * crab_distribution.get(j))
        fuel_cost[i] = fuel_cost.get(i) + fuel_expended

min_fuel_cost_location = min(fuel_cost, key=fuel_cost.get)
#print(fuel_cost)
print("The best position is", min_fuel_cost_location, "using", int(fuel_cost.get(min_fuel_cost_location)), "fuel")