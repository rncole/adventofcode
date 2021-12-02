# Advent of Code Day 6 - Customs Forms

# In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to
# the same question don't count extra; each question counts at most once.)

import pandas as pd
import functools

# infile = open('input.txt', 'r')
# groupdata = list()
# group = 1
#
# with infile as f:
#     for line in f:
#         line = line.rstrip()
#         linedict = dict()
#         linedict = "".join(dict.fromkeys(line))
#         if line != '':
#             groupdata.append([group,linedict])
#         if line == '':
#             group = group+1
#         if 'EOF' in line:
#             break
#
# groupsum = pd.DataFrame(groupdata,columns=['group','selections'])
# mergedgroupsum = groupsum.groupby('group')['selections'].apply(''.join).reset_index()
# # print(groupsum)
#
# index = mergedgroupsum.index
# rows = len(index)
# j = 0
# stringcountsum = []
# templist = []
# templist2 = []
# k = 0
# l = 0
#
# groupnum = 0
# groupmax = max(groupsum['group'])
#
# print(groupsum)
# while j < rows:
#     string = groupsum.at[j,'selections']
#     stringcount = len(sorted(set(string)))
#     stringcountsum.append([stringcount])
#     group = groupsum.at[j,'group']
#     # while k < len(string):
#     #     # newrow = []
#     #     # print(newrow)
#     #     # print(string[k])
#     #     k = k + 1
#     # else:
#     #     k = 0
#     l = l+1
#     j = j+1
#     # print(templist)
#
#     # templist = string
# print(templist)
#
#
#
# s = 0
# for line in stringcountsum:
#     s+=sum(line)

# print(mergedgroupsum)
# print(teststring)
# print(stringcountsum)
# sum = sum(stringcountsum)
# print("Sum: ",s)

# Thanks to Jeremy for helping me restructure to get the data to work much better than the above, which worked for the
# first part only.
infile = open('input.txt', 'r')
groups = []
with infile as f:
    group = []
    for line in f:
        if line != "\n":
            group.append(set(line.rstrip()))
        if line == "\n":
            groups.append(group)
            group = []
        if 'EOF' in line:
            break
    groups.append(group)
print(groups)

group_by_sets = list(map(lambda group: functools.reduce(lambda a, b: a | b, group),groups))
print(group_by_sets)
sum_by_groups = list(map(lambda group: len(group),group_by_sets))
print(sum_by_groups)
answer = functools.reduce(lambda a, b: a+b, sum_by_groups)
print(answer)

intsec_by_sets = list(map(lambda group: functools.reduce(lambda a, b: a & b, group),groups))
# print(union_by_sets)
intsec_by_groups = list(map(lambda group: len(group),intsec_by_sets))
answer = functools.reduce(lambda a, b: a+b,intsec_by_groups)
print(answer)