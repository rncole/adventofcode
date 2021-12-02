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

import check_data
line_mod = 0

print('Part 1 Accumulator Count:', check_data.check_data(line_mod, 1)[0])

while True:
    if check_data.check_data(line_mod, 0)[1] == 0:
        print('Part 2 Accumulator Count:', check_data.check_data(line_mod, 0)[0])
        break
    line_mod = line_mod + 1

