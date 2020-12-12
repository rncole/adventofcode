# Advent of Code Day 9

# Part 1:
import itertools

infile = open('input.txt', 'r')
xmas_data = []
seq = 0
xmas_vuln = []
xmas_invalid = 0
xmas_vuln_list = []

with infile as f:
    for line in f:
        xmas_data.append((seq, str.rstrip(line)))
        seq = seq + 1


def valid_comb(sum_set, check):
    return [comb for comb in itertools.combinations(sum_set, 2) if sum(comb) == check]


pair_list = []

for i in range(xmas_data[25][0], len(xmas_data)):
    check_set = list(xmas_data[i-25:i])
    check_set = [int(row[1]) for row in check_set]
    sum_to_check = int(xmas_data[i][1])
    valid_pair = valid_comb(check_set, sum_to_check)
    pair_list.append((xmas_data[i], valid_pair))

for j in range(0, len(pair_list)-1):
    if not pair_list[j][1]:
        xmas_invalid = pair_list[j][0][1]
        xmas_vuln = pair_list[j]
        print('XMAS Invalid Sequence:', xmas_invalid)

# Part 2 Start
xmas_data_vuln_id = xmas_vuln[0][0]
sum_to_check = xmas_invalid

for i in range(0, xmas_data_vuln_id-1):
    for j in range(i, len(pair_list)-1):
        check_set_vuln = list(xmas_data[i:j])
        check_set_vuln = [int(row[1]) for row in check_set_vuln]
        sum_check = sum(check_set_vuln)
        if int(sum_check) == int(xmas_invalid):
            print('Range:', i, ' to ', j)
            xmas_vuln_list = check_set_vuln

print('Min in Range:', min(xmas_vuln_list), '\nMax in Range:', max(xmas_vuln_list),
      '\nSum of Min/Max in Range:', min(xmas_vuln_list)+max(xmas_vuln_list))
