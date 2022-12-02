#!/usr/bin/python


# Advent of code 2021 challenge 3

file = open('input', 'r')

bit_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0

with file as f:
    for line in f:
        if int(line[0]) == 1:
            bit_count[0] += 1
        if int(line[1]) == 1:
            bit_count[1] += 1
        if int(line[2]) == 1:
            bit_count[2] += 1
        if int(line[3]) == 1:
            bit_count[3] += 1
        if int(line[4]) == 1:
            bit_count[4] += 1
        if int(line[5]) == 1:
            bit_count[5] += 1
        if int(line[6]) == 1:
            bit_count[6] += 1
        if int(line[7]) == 1:
            bit_count[7] += 1
        if int(line[8]) == 1:
            bit_count[8] += 1
        if int(line[9]) == 1:
            bit_count[9] += 1
        if int(line[10]) == 1:
            bit_count[10] += 1
        if int(line[11]) == 1:
            bit_count[11] += 1
        i += 1

print(bit_count, i)

digit0 = round(bit_count[0]/i)


gamma = str(round(bit_count[0]/i)) + str(round(bit_count[1]/i)) + str(round(bit_count[2]/i)) \
        + str(round(bit_count[3]/i)) + str(round(bit_count[4]/i)) + str(round(bit_count[5]/i)) \
        + str(round(bit_count[6]/i)) + str(round(bit_count[7]/i)) + str(round(bit_count[8]/i)) \
        + str(round(bit_count[9]/i)) + str(round(bit_count[10]/i)) + str(round(bit_count[11]/i))

epsilon = gamma.replace("1", "2")
epsilon = epsilon.replace("0", "1")
epsilon = epsilon.replace("2", "0")

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)


print("Gamma: ", gamma)
print("Epsilon: ", epsilon)

print("Power Consumption: ", gamma*epsilon)
