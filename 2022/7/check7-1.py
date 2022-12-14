#!/usr/bin/python
import string
# Advent of code 2022 challenge 2
import string as st
import functools

file = open('input', 'r')
file_table = []

with file as f:
    for line in f:
        line = line.strip()
        if line[0] == '$':
            #print("command detected:", line[2:])
            cur_command = line[2:4]
            if cur_command == 'cd':
                cd_loc = line[5:]
                if cd_loc == '/':
                    current_path = '/'
                elif cd_loc == '..':
                    prev_dir_char_pos = current_path.rfind('/', 0, -1)
                    current_path = current_path[:prev_dir_char_pos+1]
                else:
                    current_path = current_path+cd_loc+'/'
        elif line[:3] == 'dir':
            dir_entry = line[4:]
            file_table.append([current_path, 'dir', dir_entry])
            print("Directory:", dir_entry)
        else:
            file_entry = line.split(' ')
            print("File:", file_entry)
            file_table.append([current_path, 'file', file_entry])

print(file_table)

directory_sizes = [['/', 0]]

for each in file_table:
    if each[1] == 'dir':
        directory_sizes.append([str(each[0]+each[2]+'/'), 0])

print(directory_sizes)
cur_dir = ''

for each in file_table:
    if each[1] == 'file':
        parent_folder = each[0]
        for cur_dir in directory_sizes:
            cur_dir_path = cur_dir[0]
            if parent_folder.startswith(cur_dir_path):
                print("current dir:", cur_dir, "Parent folder", parent_folder)
                cur_dir_index = directory_sizes.index(cur_dir)
                cur_dir = [cur_dir_path, cur_dir[1]+int(each[2][0])]
                print("Adding", each[2][1], "with path", each[0], "to path", cur_dir_path)
                print("Current Directory:", cur_dir)
                directory_sizes[cur_dir_index] = cur_dir

size_sum = 0

for each in directory_sizes:
    if each[1] <= 100000:
        size_sum += each[1]

print("\nThe sum of folders <= 100000 is:", size_sum)

drive_size = 70000000
min_free = 30000000
directory_sizes.sort()
drive_used = directory_sizes[0][1]
drive_free = drive_size-drive_used
print("Drive used:", drive_used, "Space Free:", drive_size-drive_used)
potential_del = []

for each in directory_sizes:
    if drive_free + each[1] >= min_free:
        potential_del.append(each)
potential_del.sort(key=lambda x:x[1])

print("Potential Deletions:", potential_del)
