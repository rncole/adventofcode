# Advent of Code Day 6 - Customs Forms

# In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to
# the same question don't count extra; each question counts at most once.)

import pandas as pd

infile = open('input.txt', 'r')
groupdata = list()
group = 1

with infile as f:
    for line in f:
        line = line.rstrip()
        linedict = dict()
        linedict = "".join(dict.fromkeys(line))
        if line != '':
            groupdata.append([group,linedict])
        if line == '':
            group = group+1
        if 'EOF' in line:
            break

groupsum = pd.DataFrame(groupdata,columns=['group','selections'])
mergedgroupsum = groupsum.groupby('group')['selections'].apply(''.join).reset_index()

index = mergedgroupsum.index
rows = len(index)
j = 0
stringcountsum = []

while j < rows:
    string = mergedgroupsum.at[j,'selections']
    stringcount = len(sorted(set(string)))
    stringcountsum.append([stringcount])
    j = j + 1

s = 0
for line in stringcountsum:
    s+=sum(line)

# print(mergedgroupsum)
# print(teststring)
# print(stringcountsum)
# sum = sum(stringcountsum)
print("Sum: ",s)

