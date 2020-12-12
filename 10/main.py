# Advent of Code Day 10: Python Solution

# Part 1:
infile = open('input.txt','r')
adapters = []

with infile as f:
    for line in f:
        adapters.append(str.rstrip(line))

adapters.append('0')
adapters = list(map(int, adapters))
adapters.sort()
adapters.append(max(adapters) + 3)
# print(adapters)
# print(adapters[3])

adapters_1jolt = 0
adapters_3jolt = 0

for i in range(0,len(adapters)-1):
    if adapters[i+1] - adapters[i] == 1:
        adapters_1jolt = adapters_1jolt + 1
    if adapters[i+1] - adapters[i] == 3:
        adapters_3jolt = adapters_3jolt + 1
print('1-Jolt Adapters:', adapters_1jolt, '\n3-Jolt Adapters:', adapters_3jolt)
print('Solution:', adapters_1jolt * adapters_3jolt)
