# Advent of Code Day 9

# Part 1:
import itertools

infile = open('input.txt', 'r')
xmas_data = []
seq = 0

with infile as f:
    for line in f:
        xmas_data.append((seq,str.rstrip(line)))
        seq = seq + 1

def valid_comb(check_set,sum_to_check):
    return [comb for comb in itertools.combinations(check_set,2) if sum(comb) == sum_to_check]

pair_list = []

for i in range(xmas_data[25][0],len(xmas_data)):
    check_set = list(xmas_data[i-25:i])
    check_set = [int(row[1]) for row in check_set]
    sum_to_check = int(xmas_data[i][1])
    valid_pair = valid_comb(check_set,sum_to_check)
    pair_list.append((xmas_data[i],valid_pair))

for j in range(0,len(pair_list)-1):
    if not pair_list[j][1]:
        xmas_invalid = pair_list[j][0][1]
        print('XMAS Invalid Sequence:',xmas_invalid)

# Part 2 Start
# for k in range(0,pair_list[]):
#     xmas_data_curr = xmas_data[k][1]
#     xmas_data_prev = xmas_data[k-1][1]
#     sum_invalid = xmas_data_curr + xmas_data_prev
#     if sum_invalid == xmas_invalid:
#         print('Sum of Invalid:',sum_invalid)
