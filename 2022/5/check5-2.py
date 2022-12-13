#!/usr/bin/python
import string
# Advent of code 2022 challenge 2
import string as st
import functools

file = open('input', 'r')
section = 0
stack = 1
from_start = 0
to_start = 0
# Stacks are in format of [stack0, stack1, ... stack{n}] where stack{n} = [position, crate]
stacks = []
stack_pos = 0

with file as f:
    for line in f:
        if section == 1:
            from_start = line.find(" from ")
            to_start = line.find(" to ")
            move_qty = int(line[5:from_start])
            from_loc = int(line[from_start+6:to_start])
            to_loc = int(line[to_start+4:])
            print("moving", move_qty, "from", from_loc, "to", to_loc)
            cur_from_stack = stacks[from_loc-1][1]
            cur_to_stack = stacks[to_loc-1][1]
            new_from_stack = [from_loc, cur_from_stack[:-move_qty]]
            moved_crates = cur_from_stack[-move_qty:]
            # moved_crates.reverse()
            new_to_stack = [to_loc, cur_to_stack+moved_crates]
            del stacks[from_loc-1]
            stacks.append(new_from_stack)
            stacks.sort()
            del stacks[to_loc-1]
            stacks.append(new_to_stack)
            stacks.sort()
            #print(stacks)
        if line == "\n":
            print("\nNext Section Start\n")
            section += 1
        if line[:2] == " 1":
            continue
        if section == 0:
            line_slicer = line
            while(len(line) >= 4):
                crate = line_slicer[:4]
                if crate != "    ":
                    crate = crate.strip()
                    print("Stack:", stack, "has crate", crate, "at position", stack_pos)
                    stack_list = [i[0] for i in stacks]
                    if stack in stack_list:
                        stack_index = stacks[0].index(stack)
                        cur_stack = stacks[stack_index][1]
                        cur_stack.insert(0, crate)
                        new_stack = [stack, cur_stack]
                        del stacks[stack_index]
                        stacks.append(new_stack)
                    else:
                        stacks.append([stack, [crate]])
                line_slicer = line[4:]
                line = line_slicer
                stack += 1
            stack_pos += -1
        stack = 1
        stacks.sort()

print(stacks)

crate_code = ''
for each in stacks:
    crate_code = crate_code+each[1][-1].strip('[]')

print("\nThe Topmost Crates are:", crate_code)
