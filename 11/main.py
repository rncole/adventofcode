# Advent of Code Day 11: Seating System
import copy
import functools

infile = open('input.txt','r')

seating_map_tmp = []
with infile as f:
    for line in f:
        line = line.rstrip()
        seating_map_tmp.append(line)
seating_map = [list(sub) for sub in seating_map_tmp]
seating_map_tmp = copy.deepcopy(seating_map)

# print(seating_map)
# print(seating_map_tmp)
# print(seating_map)


def seatingmap_update():
    adj_count = 0
    for row in range(0, len(seating_map_tmp)):
        for col in range(0, len(line)):
            if seating_map_tmp[row][col] == 'L':
                # print('Found Empty Seat:',row,',',col, seating_map_tmp[row][col], seating_map[row][col])
                # print('row_len:', len(seating_map_tmp[row]))
                if row != len(seating_map_tmp)-1:
                    if seating_map_tmp[row + 1][col] == '#':
                        adj_count = adj_count + 1
                if row != 0:
                    if seating_map_tmp[row - 1][col] == '#':
                        adj_count = adj_count + 1
                if col != len(seating_map_tmp[row])-1:
                    if seating_map_tmp[row][col + 1] == '#':
                        adj_count = adj_count + 1
                if col != 0:
                    if seating_map_tmp[row][col - 1] == '#':
                        adj_count = adj_count + 1
                if row != len(seating_map_tmp)-1 and col != len(seating_map_tmp[row])-1:
                    if seating_map_tmp[row + 1][col + 1] == '#':
                        adj_count = adj_count + 1
                if row != len(seating_map_tmp)-1 and col != 0:
                    if seating_map_tmp[row + 1][col - 1] == '#':
                        adj_count = adj_count + 1
                if row != 0 and col != len(seating_map_tmp[row])-1:
                    if seating_map_tmp[row - 1][col + 1] == '#':
                        adj_count = adj_count + 1
                if row != 0 and col != 0:
                    if seating_map_tmp[row - 1][col - 1] == '#':
                        adj_count = adj_count + 1
                # print('Empty Adj Count:',adj_count)
                if adj_count == 0:
                    seating_map[row][col] = '#'
                    # print('Filling Seat:',row,',',col)
                adj_count = 0
            if seating_map_tmp[row][col] == '#':
                # print('Found Filled Seat:',row,',',col, seating_map_tmp[row][col], seating_map[row][col])
                if row != len(seating_map_tmp)-1:
                    if seating_map_tmp[row + 1][col] == '#':
                        adj_count = adj_count + 1
                if row != 0:
                    if seating_map_tmp[row - 1][col] == '#':
                        adj_count = adj_count + 1
                if col != len(seating_map_tmp[row]) - 1:
                    if seating_map_tmp[row][col + 1] == '#':
                        adj_count = adj_count + 1
                if col != 0:
                    if seating_map_tmp[row][col - 1] == '#':
                        adj_count = adj_count + 1
                if row != len(seating_map_tmp) - 1 and col != len(seating_map_tmp[row]) - 1:
                    if seating_map_tmp[row + 1][col + 1] == '#':
                        adj_count = adj_count + 1
                if row != len(seating_map_tmp) - 1 and col != 0:
                    if seating_map_tmp[row + 1][col - 1] == '#':
                        adj_count = adj_count + 1
                if row != 0 and col != len(seating_map_tmp[row]) - 1:
                    if seating_map_tmp[row - 1][col + 1] == '#':
                        adj_count = adj_count + 1
                if row != 0 and col != 0:
                    if seating_map_tmp[row - 1][col - 1] == '#':
                        adj_count = adj_count + 1
                # print('Occ Adj. Count:',adj_count)
                if adj_count >= 4:
                    seating_map[row][col] = 'L'
                    # print('Emptying Seat:',row,',',col)
                adj_count = 0
        # print(seating_map)
        # print(seating_map_tmp)


seating_unchanged = 0
iteration_count = 0

while seating_unchanged == 0:
    seating_map_tmp = copy.deepcopy(seating_map)
    seatingmap_update()
    if seating_map_tmp == seating_map:
        seating_unchanged = 1
    # print(seating_map_tmp)
    # print(seating_map)
    iteration_count = iteration_count + 1

# print(iteration_count)
# print(seating_map)

occupied_count = 0

for row in range(0, len(seating_map)):
    for col in range(0, len(line)):
        if seating_map[row][col] == '#':
            occupied_count = occupied_count + 1

print('Occupied Seats = ', occupied_count)

# Fancier way to do the above:
# occupied_reduce_full = functools.reduce(lambda sum_hash, row: sum_hash + (functools.reduce(lambda sum_hash, item: sum_hash + (1 if item == '#' else 0), row, 0)), seating_map, 0)
#
# occupied_reduce = functools.reduce(lambda sum_hash, item: sum_hash + (1 if item == '#' else 0), seating_map[0], 0)
#
# print(seating_map[0])
# print(occupied_reduce_full)

