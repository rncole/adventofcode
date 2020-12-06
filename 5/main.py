# Advent of Code Day 5: Seat Finder
#
# For example, consider just the first seven characters of FBFBBFFRLR:
#
# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
#
# Seat Location Format:
# FBFBBFFRLR
# Every seat also has a unique seat ID: multiply the row by 8, then add the column.
# In this example, the seat has ID 44 * 8 + 5 = 357.

infile = open('input.txt', 'r')
newlineset = set()
lineset = set()
lineintset = set()

with infile as f:
    for line in f:
        line = line.strip(' ')
        line = line.rstrip()
        newline = line
        newline = newline.replace('F','0')
        newline = newline.replace('B','1')
        newline = newline.replace('L','0')
        newline = newline.replace('R','1')
        lineint = int(newline,2)
        lineset.update([line])
        newlineset.update([newline])
        lineintset.update([lineint])
        # print(line)
        # print(newline)
        # print(lineint)
        if 'str' in line:
            break

lineintset = sorted(lineintset)
missingseat = sorted(set(range(min(lineintset),max(lineintset))) - set(lineintset))

print("The Max Seat Location is: ",max(lineintset))
print("The Missing Seat Location(s) are: ",missingseat)

