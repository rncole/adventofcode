# Advent of Code Day 7 - Handheld Halting
# The boot code is represented as a text file with one instruction per line of text.
# Each instruction consists of an operation (acc, jmp, or nop) and an argument (a
# signed number like +4 or -20).
#
# acc increases or decreases a single global value called the accumulator by the value
# given in the argument. For example, acc +7 would increase the accumulator by 7. The
# accumulator starts at 0. After an acc instruction, the instruction immediately below
# it is executed next.
#
# jmp jumps to a new instruction relative to itself. The next instruction to execute
# is found using the argument as an offset from the jmp instruction; for example,
# jmp +2 would skip the next instruction, jmp +1 would continue to the instruction
# immediately below it, and jmp -20 would cause the instruction 20 lines above to be
# executed next.

# nop stands for No OPeration - it does nothing. The instruction immediately below it
# is executed next.


infile = open('input.txt','r')
acc_count = 0
op_num = 0
operation = []

with infile as f:
    for line in f:
        operation.append((op_num,[line.partition(' ')[0],str.rstrip(line.partition(' ')[2])]))
        op_num = op_num+1
        if 'EOF' in line:
            break

op_completed = []
curr_op_num = 0
loop_control = True
line_to_change = 0
last_line_changed = 0
change_count = 0
curr_op1 = []

def change_op(curr_op):
    if curr_op == 'nop':
       curr_op = 'jmp'
    if curr_op == 'jmp':
       curr_op = 'nop'
    if curr_op == 'acc':
       curr_op = 'acc'
    return(curr_op)

while loop_control:
    # print(curr_op_num)
    # print(acc_count)
    # print(operation)
    if curr_op_num == len(operation):
        print('Accumulator:', acc_count)
        break
    print(acc_count)
    print(operation[curr_op_num])
    curr_op = operation[curr_op_num][1][0]
    # print(op_completed)
    if curr_op_num not in op_completed:
        if curr_op == 'acc':
            acc_inc = int(operation[curr_op_num][1][1])
            acc_count = acc_count + acc_inc
            op_completed.append(curr_op_num)
            curr_op_num = curr_op_num + 1
        if curr_op == 'jmp':
            op_completed.append(curr_op_num)
            curr_op_num = curr_op_num + int(operation[curr_op_num][1][1])
        if curr_op == 'nop':
            curr_op_num = curr_op_num + 1
        # print(op_completed)
    else:
        print('Still Broken')
        print('Accumulator:', acc_count)
        print('Operation:', operation[line_to_change])
        print('Line:', line_to_change)
        if change_count == 20:
            break
        op_completed = []
        acc_count = 0
        line_to_change_prev = line_to_change - 1
        print('Prev Line:',line_to_change_prev)
        print('prev_op',curr_op1)
        operation.insert(line_to_change_prev,curr_op1)
        curr_op1 = operation[line_to_change]
        print(operation)
        curr_op = operation[line_to_change][1][0]
        curr_op_line = (line_to_change,[change_op(curr_op),operation[curr_op_num][1][1]])
        operation.insert(line_to_change,curr_op_line)
        change_count = change_count +1
        print('Operation New:',operation[line_to_change])
        line_to_change = line_to_change + 1
        curr_op = 0

print(op_completed)
print('Accumulator:',acc_count)
print(len(operation))

# if line.partition(' ')[0] == 'acc':
# acc_count = acc_count line.partition(' ')[2]
# if line.partition(' ')[0] == 'jmp':
