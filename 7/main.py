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
        if inner_bag_tmp == 'no other':
            outer_bag.append((outer_bag_tmp,[]))
        else:
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


outer_bag_dict = dict(outer_bag)
def retr_inner_bags(color,inner_bags,multiplier=1):
    for inner_bag in outer_bag_dict[color]:
        inner_bags.append([inner_bag[0][0]*multiplier,inner_bag[1]])
        retr_inner_bags(inner_bag[1],inner_bags,inner_bag[0][0]*multiplier)
    return inner_bags

inner_bags = retr_inner_bags('shiny gold',[],1)

inner_bag_sum = functools.reduce(lambda a,b: a+b,list(map(lambda a:a[0],inner_bags)))

print('Shiny Bag Contains:',inner_bag_sum,'bags')