# Advent of Code Day 9

infile = open('input.txt', 'r')
xmas_data = []
seq = 0

with infile as f:
    for line in f:
        xmas_data.append((seq,str.rstrip(line)))
        seq = seq + 1

print(xmas_data)
loop_test = [0,([0],[0])]
loop = 0
loop_test_dict = dict()
start_offset = 0
# start_seq = xmas_data[]+start_offset
counter = 0
loop_control = True

while loop_control == True:
    for x in range(start_offset,start_offset+25):
        if start_offset+25 >= len(xmas_data)-24:
            loop_control = False
        for y in range(0,24):
            xmas_data_sum = int(xmas_data[start_offset+24][1])
            x = x+1
            xmas_data_sum_try = int(xmas_data[start_offset+y][1]) + int(xmas_data[x][1])
            counter = counter + 1
            # print('counter:',counter,'  sum:',xmas_data_sum,'trying',xmas_data[start_offset][1],'and',xmas_data[x][1],'equals',xmas_data_sum_try)
            if xmas_data_sum == xmas_data_sum_try:
                # print('Sum of',xmas_data[start_offset],'and',xmas_data[x],'valid')
                loop_valid_count = loop_test[0]
                loop_valid_count = loop_valid_count + 1
                # del loop_test[loop]
                # print([loop,xmas_data_sum,loop_valid_count])
                loop_test.append([xmas_data[start_offset+24][0],([xmas_data_sum],[loop_valid_count])])
                loop_test_dict[loop] = xmas_data[start_offset+24][0]
    loop = loop + 1
    start_offset = start_offset + 1
print(loop_test)


print('test:',loop_test[3][0])
print(loop_test_dict)
j = 0

for key, value in loop_test_dict.items():
    if key != j:
        print(j)
        print(key,value)
    j = j +1

# print(loop_test_dict.keys[j])
# if loop_test_dict.keys[j] != j+1:
#     print(loop_test_dict[j])

# while j < len(loop_test_dict):
#     print('Checking for',j,loop_test_dict.get(j))
#
#         print('yay')
#     j = j+1
#     loop_count = x
#     loop_count_last = x-1
#     print(loop_test[loop_count])
#     loop_test_int = loop_test[loop_count]
#     if loop_count > loop_test_int:
#         print('Last Good Value:',loop_test[loop_count_last])
#     x = x + 1
#
