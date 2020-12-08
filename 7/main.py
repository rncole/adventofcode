# Advent of Code Day 7 - issues in luggage processing

import functools

infile = open('input.txt','r')
groups = []
outer_cont_sg = []
outer_bag = []
inner_bags = []

with infile as f:
    for line in f:
        outer_bag_tmp = line.partition(' bags contain ')[0]
        inner_bag_tmp = line.partition(' bags contain ')[2]
        inner_bag_tmp = inner_bag_tmp.replace('bags','')
        inner_bag_tmp = inner_bag_tmp.replace('bag','')
        inner_bag_tmp = inner_bag_tmp.replace('.','')
        inner_bag_tmp = inner_bag_tmp.rstrip()
        inner_bag_tmp_list = inner_bag_tmp.split(',')
        inner_bag_tmp_list = [s.strip() for s in inner_bag_tmp_list]
        for index, each in enumerate(inner_bag_tmp_list):
            bag_qty = [int(s) for s in each.split() if s.isdigit()]
            if bag_qty != 0:
                bag_desc = each.partition(' ')[2]
                inner_bag_tmp_list[index] = bag_qty,bag_desc
            else:
                bag_desc = each
                inner_bag_tmp_list[index] = bag_qty,bag_desc
        bag_set = outer_bag_tmp,inner_bag_tmp_list
        outer_bag.append(bag_set)
        if 'EOF' in line:
            break

for i,each in enumerate(outer_bag):
    inner_bag_count = len(outer_bag[i][1])
    # print("Outer Bag:",outer_bag[i][0],"contains",inner_bag_count,"inner bag color(s):")
    j = 0
    while j < inner_bag_count:
        # print(outer_bag[i][1][j][1])
        if outer_bag[i][1][j][1] == ("shiny gold"):
            outer_cont_sg.append(outer_bag[i][0])
        j = j+1

recursion_complete = 0
bag_recursion_count = len(outer_cont_sg)
bag_recursion_count_diff = 0
bag_recursion_count_diff_prev = 1

while recursion_complete == 0:
    for i, each in enumerate(outer_bag):
        inner_bag_count = len(outer_bag[i][1])
        # print("Outer Bag:", outer_bag[i][0], "contains", inner_bag_count, "inner bag color(s):")
        j = 0
        while j < inner_bag_count:
            # print(outer_bag[i][1][j][1])
            if outer_bag[i][1][j][1] in outer_cont_sg:
                outer_cont_sg.append(outer_bag[i][0])
            j = j + 1
        bag_recursion_count_diff = len(outer_cont_sg) - bag_recursion_count

    if bag_recursion_count_diff == bag_recursion_count_diff_prev:
        recursion_complete = 1
    else:
        outer_cont_sg = list(dict.fromkeys(outer_cont_sg))
        bag_recursion_count = len(outer_cont_sg)
        bag_recursion_count_diff_prev = bag_recursion_count_diff
        # print(bag_recursion_count)

print("\nTotal Bags:",len(outer_bag))
outer_cont_sg = list(dict.fromkeys(outer_cont_sg))
print("Contain Shiny Gold:",len(outer_cont_sg))

bag_set_outermost = ['shiny gold','wavy chartreuse']
bag_set_middle = []
bag_set_innermost = []
bag_set_tmp = bag_set_outermost
bag_set_tmp2 = []
bag_set_tmp3 = []
bag_set_qty = []
inner_bags = []
recursion_complete = 0
bag_recursion_count = len(outer_cont_sg)
bag_recursion_count_diff = 0
bag_recursion_count_diff_prev = 0
i = 0
j = 0

print(outer_bag)
outer_bag_dict = dict(outer_bag)
print(outer_bag_dict)
for each in bag_set_tmp:
    bag_set_tmp_str = each
    inner_bags.append(outer_bag_dict[bag_set_tmp_str])
print(inner_bags)


# while recursion_complete == 0:
# for i, each in enumerate(outer_bag)
#     inner_bag_count = len(outer_bag[i][1])
#     print(outer_bag[i][1])
#     print(inner_bag_count)
#     if outer_bag[i][1] in bag_set_tmp:
#         print(outer_bag[i][1])
#         if inner_bag_count == '0':
#             while j < inner_bag_count:
#                 bag_set_tmp2.append(outer_bag[i][1][j][1])
#                 j = j + 1
#             bag_set_tmp = bag_set_tmp2
#         else:
#             bag_set_tmp3.append(bag_set_tmp)
#     # if
# print(bag_set_tmp)
# print(bag_set_tmp2)
# print(bag_set_tmp3)






        # for j, each in enumerate(outer_bag):
        #     print("i =",i)
        #     print("j =",j)
        #     print(bag_set_tmp)
        #     if outer_bag[j][0] in bag_set_tmp:
        #         bag_set_tmp2 = outer_bag[i][1][j][0],outer_bag[i][1][j][1]
        #         print(bag_set_tmp2)
        #         bag_set_tmp3.append(bag_set_tmp2)
        #         bag_set_tmp = bag_set_tmp2
        #         bag_set_tmp2 = []
        #     j = j+1
        # i = i+1
        # j = 0
        # print(bag_set_tmp3)




# while recursion_complete == 0:
#     for i, each in enumerate(outer_bag):
#         # bag_set_tmp_qty = len(outer_bag[i][1])
#         # print(bag_set_tmp_qty)
#         j = 0
#         while j < len(outer_bag[i][1]):
#             if outer_bag[i][0] in bag_set_tmp:
#                 bag_set_tmp = outer_bag[i][1][j][1]
#                 bag_set_qty_tmpval = outer_bag[i][1][j][0]
#                 # print("val:",bag_set_qty_tmpval)
#                 # print(outer_bag[i][0])
#                 # if outer_bag[i][0] != 'shiny gold':
#                 print(bag_set_tmp)
#                 print(bag_set_qty_tmpval)
#                 # print(outer_bag[i][1][j][1])
#                     # bag_set_qty_tmpval_int = int(bag_set_qty_tmpval[1])
#                     # if bag_set_qty_tmpval == []:
#                     #     bag_set_qty_tmpval = [1]
#                 bag_set_qty.append(bag_set_qty_tmpval)
#                 # print("int:",bag_set_qty_tmpval_int)
#                 # print(bag_set)
#             j = j+1
#             bag_recursion_count_diff = len(bag_set) - bag_recursion_count
#
#     if bag_recursion_count_diff == bag_recursion_count_diff_prev:
#         recursion_complete = 1
#     else:
#         bag_set = list(dict.fromkeys(bag_set))
#         bag_recursion_count = len(bag_set)
#         bag_recursion_count_diff_prev = bag_recursion_count_diff
#         # print(bag_recursion_count)
# print(bag_set)
# print(bag_set_qty)
# print(bag_set_qty)
# bag_set_qty_sum = functools.reduce(lambda a,b: a + b,bag_set_qty)
# bag_set_qty_sum = functools.reduce(lambda a,b: a + b,bag_set_qty_sum)
# print("Bags inside Shiny Gold:",bag_set_qty_sum)
