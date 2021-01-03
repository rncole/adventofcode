# Advent of Code Day 15
import copy

input = [7, 12, 1, 0, 16, 2]

# Rules:
# 1. If that was the first time the number has been spoken, the current player says 0.
#
# 2. Otherwise, the number had been spoken before; the current player announces how many turns apart the number
# is from when it was previously spoken.

count = 6

print('test:',len(input) - 1 - input[::-1].index(16))

while count <= 20:
    # print(input[count-1])
    # print(input[0:count-1])
    list_tmp = copy.deepcopy(input[0:count-1])
    print('Tmp List:',list_tmp)
    check_val = input[count-1]
    print('Value to Check:',check_val)
    # print(range(len(list_tmp)))
    try:
        next(i for i in reversed(range(len(list_tmp))) if list_tmp[i] == check_val)
        input.append(0)
        print('New Not Exist:',0)
    except StopIteration:
        new_val = (count-1) - (len(input) - 1 - input[::-1].index(check_val))
        print('New:',new_val)
        input.append(new_val)

    count = count + 1
    # list_rindex((input,input))
