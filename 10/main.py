# Advent of Code Day 10: Python Solution

# Part 1:
import functools

infile = open('input.txt', 'r')
adapters = []

with infile as f:
    for line in f:
        adapters.append(str.rstrip(line))

adapters.append('0')
adapters = list(map(int, adapters))
adapters.append(max(adapters) + 3)
adapters.sort()

adapters_1jolt = 0
adapters_3jolt = 0

adapters_with_diff = []

for i in range(0, len(adapters)-1):
    if adapters[i+1] - adapters[i] == 1:
        adapters_1jolt = adapters_1jolt + 1
        adapters_with_diff.append([adapters[i+1], 1])
    if adapters[i+1] - adapters[i] == 3:
        adapters_3jolt = adapters_3jolt + 1
        adapters_with_diff.append([adapters[i+1], 3])
print('1-Jolt Adapters:', adapters_1jolt, '\n3-Jolt Adapters:', adapters_3jolt)
print('Solution:', adapters_1jolt * adapters_3jolt)

seq_count = 0
adapters_with_diff_seq = []

for j in range(0, len(adapters_with_diff)-1):
    if adapters_with_diff[j][1] == 1:
        seq_count = seq_count + 1
    if adapters_with_diff[j][1] == 3:
        seq_count = 0
    adapters_with_diff_seq.append([adapters_with_diff[j][0], adapters_with_diff[j][1], seq_count])

combo_count = []
for k in range(0, len(adapters_with_diff_seq)-1):
    if int(adapters_with_diff_seq[k+1][2]) == 0 and int(adapters_with_diff_seq[k][2]) != 0:
        if int(adapters_with_diff_seq[k][2]) == 1:
            combo_count.append(1)
        if int(adapters_with_diff_seq[k][2]) == 2:
            combo_count.append(2)
        if int(adapters_with_diff_seq[k][2]) == 3:
            combo_count.append(4)
        if int(adapters_with_diff_seq[k][2]) == 4:
            combo_count.append(7)

print('Part 2 Solution:', functools.reduce((lambda a, b: a*b), combo_count))
