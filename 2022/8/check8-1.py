#!/usr/bin/python
import string
# Advent of code 2022 challenge 2
import string as st
import functools
import numpy as np

file = open('input', 'r')
row = []
first = 0

with file as f:
    for line in f:
        for char in line.strip('\n'):
            row.append(int(char))
            #print(row)
        if first == 0:
            map = row
        else:
            map = np.vstack([map, row])
        first = 1
        row = []
print(map)

map_shape = map.shape
map_x_dim = map.shape[0]-1
map_y_dim = map.shape[1]-1

print(map_shape, map_x_dim, map_y_dim)

cur_x_pos = 0
cur_y_pos = 0
tree_visible = np.zeros(map_shape)
tree_visible_n = np.zeros(map_shape)
tree_visible_s = np.zeros(map_shape)
tree_visible_e = np.zeros(map_shape)
tree_visible_w = np.zeros(map_shape)

for row in map:
    for tree in row:
        if cur_x_pos == 0 or cur_x_pos == map_x_dim:
            tree_visible[cur_y_pos, cur_x_pos] = 1
        elif cur_y_pos == 0 or cur_y_pos == map_y_dim:
            tree_visible[cur_y_pos, cur_x_pos] = 1
        # Check North
        else:
            for n_trees in range(cur_y_pos):
                if tree <= map[n_trees, cur_x_pos]:
                    tree_visible_n[cur_y_pos, cur_x_pos] = 0
                    break
                else:
                    tree_visible_n[cur_y_pos, cur_x_pos] = 1
            for s_trees in range(cur_y_pos+1, map_y_dim+1):
                if tree <= map[s_trees, cur_x_pos]:
                    tree_visible_s[cur_y_pos, cur_x_pos] = 0
                    break
                else:
                    tree_visible_s[cur_y_pos, cur_x_pos] = 1
            for w_trees in range(cur_x_pos):
                if tree <= map[cur_y_pos, w_trees]:
                    tree_visible_w[cur_y_pos, cur_x_pos] = 0
                    break
                else:
                    tree_visible_w[cur_y_pos, cur_x_pos] = 1
            for e_trees in range(cur_x_pos+1, map_x_dim+1):
                if tree <= map[cur_y_pos, e_trees]:
                    tree_visible_e[cur_y_pos, cur_x_pos] = 0
                    break
                else:
                    tree_visible_e[cur_x_pos, cur_y_pos] = 1
        cur_x_pos += 1
    cur_x_pos = 0
    cur_y_pos += 1

tree_visible = tree_visible + tree_visible_n + tree_visible_s + tree_visible_e + tree_visible_w
print(tree_visible)
#print("North:\n", tree_visible_n)
#print("South:\n", tree_visible_s)
#print("East:\n", tree_visible_e)
#print("West:\n", tree_visible_w)


print("There are ", np.count_nonzero(tree_visible), "trees visible.")