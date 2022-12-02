#!/usr/bin/python


# Advent of code 2021 challenge 3
import string as st
import functools

file = open('input', 'r')

bit_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
o2_gen = []

with file as f:
    for line in f:
        o2_gen.append(line.strip())
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

co2_scr = o2_gen

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

print("-------")
print("Part 1:")
print("-------")

print("Gamma: ", gamma)
print("Epsilon: ", epsilon)

print("Power Consumption: ", gamma*epsilon)

j = 0
k = 0
l = 0
m = 0
freq = 0

o2_gen_test = []

while k < len(o2_gen[0]):
    while j < len(o2_gen):
        o2_gen_test.append([o2_gen[j], int(o2_gen[j][k])])
        j += 1

    while l < len(o2_gen_test):
        freq += o2_gen_test[l][1]
        l += 1

    o2_gen = []

    while m < len(o2_gen_test):
        if freq < len(o2_gen_test)/2:
            if o2_gen_test[m][1] == 0:
                o2_gen.append(o2_gen_test[m][0])
        else:
            if o2_gen_test[m][1] == 1:
                o2_gen.append(o2_gen_test[m][0])

        m += 1


    o2_gen_test = []
    freq = 0
    k += 1
    j = 0
    l = 0
    m = 0

print("-------")
print("Part 2:")
print("-------")
print("O2 Generator Rating:", int(o2_gen[0], 2))

j = 0
k = 0
l = 0
m = 0
freq = 0

co2_scr_test = []
co2_scr_check = co2_scr

while k < len(co2_scr[0]):
    if len(co2_scr_check) > 1:
        while j < len(co2_scr):
            co2_scr_test.append([co2_scr[j], int(co2_scr[j][k])])
            j += 1

        while l < len(co2_scr_test):
            freq += co2_scr_test[l][1]
            l += 1

        co2_scr = []

        while m < len(co2_scr_test):
            if freq >= len(co2_scr_test)/2:
                if co2_scr_test[m][1] == 0:
                    co2_scr.append(co2_scr_test[m][0])
            else:
                if co2_scr_test[m][1] == 1:
                    co2_scr.append(co2_scr_test[m][0])
            m += 1
        co2_scr_check = co2_scr
    co2_scr_test = []
    freq = 0
    k += 1
    j = 0
    l = 0
    m = 0

print("CO2 Scrubber Rating:", int(co2_scr[0], 2))
print("Life Support Rating:", int(co2_scr[0], 2)*int(o2_gen[0], 2))