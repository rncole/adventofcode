#!/usr/bin/python

# Advent of code 2021 challenge 8
import math

#file = open('input', 'r')
file = open('sample', 'r')

input = []
unique_count = 0
i = 0
with file as f:
    input = f.readlines()

display_data_raw = []
for each in input:
    data = each.strip()
    data = data.split(' | ')
    display_data_raw.append(data)

i = 0
while i < len(display_data_raw):
    display = display_data_raw[i][1]
    display = display.split(' ')
    for j in range(0,len(display)):
        if len(display[j]) == 2 or len(display[j]) == 4 or len(display[j]) == 3 or len(display[j]) == 7:
            #print("adding 1 to count for", display[j])
            unique_count += 1
        j += 1
    i += 1
print("Segments for 1, 4, 6, and 8 appear", unique_count, "times.")
sum_values = 0
i = 0
while i < len(display_data_raw):
    input_string = display_data_raw[i][0]
    input_string = input_string.split(' ')
    display = display_data_raw[i][1]
    display = display.split(' ')

    input_string_values = {}
    for j in range(0,len(input_string)):
        key = input_string[j]
        input_string_values[key] = len(input_string[j])
    display_value = {}
    input_translation = {}
    for string, length in input_string_values.items():
        if length == 2:
            display_value[1] = [set(string), string]
        if length == 3:
            display_value[7] = [set(string), string]
        if length == 4:
            display_value[4] = [set(string), string]
        if length == 7:
            display_value[8] = [set(string), string]
    right_chars = display_value[1][0]
    #print(display_value[1][0])
    #print(right_chars)
    print(input_string_values)
    print(display_value)
    for string, length in input_string_values.items():
        if length == 5 and sum([characters in right_chars for characters in string]) == len(right_chars):
            print("match 3:", string)
            display_value[3] = [set(string), string]
    print(display_value)

    left_chars = display_value[8][0].symmetric_difference(display_value[3][0])
    #print("left:", left_chars)
    top_char = display_value[7][0].symmetric_difference(display_value[1][0])
    #print("top:", top_char)
    #print("left:", left_chars)

    for string, length in input_string_values.items():
        if length == 6 and sum([characters in right_chars for characters in string]) + \
                sum([characters in left_chars for characters in string]) + \
                sum([characters in top_char for characters in string]) == len(right_chars) + len(top_char) + len(left_chars):
            display_value[0] = [set(string), string]

    middle_char = display_value[8][0].symmetric_difference(display_value[0][0])
    #print("middle:", middle_char)

    for string, length in input_string_values.items():
        if length == 6 and sum([characters in right_chars for characters in string]) + \
                sum([characters in middle_char for characters in string]) + \
                sum([characters in top_char for characters in string]) == len(right_chars) + len(middle_char) + len(top_char):
            display_value[9] = [set(string), string]

    for string, length in input_string_values.items():
        if length == 6 and sum([characters in left_chars for characters in string]) + \
                sum([characters in middle_char for characters in string]) + \
                sum([characters in top_char for characters in string]) == len(left_chars) + len(middle_char) + len(top_char):
            display_value[6] = [set(string), string]

    left_bot = display_value[8][0].symmetric_difference(display_value[9][0])
    #print("left bottom:", left_bot)
    right_top = display_value[8][0].symmetric_difference(display_value[6][0])

    for string, length in input_string_values.items():
        if length == 5 and sum([characters in left_bot for characters in string]) + \
                sum([characters in middle_char for characters in string]) + \
                sum([characters in top_char for characters in string]) == len(left_bot) + len(middle_char) + len(top_char):
            display_value[2] = [set(string), string]

    right_bot = right_chars.symmetric_difference(right_top)
    #print("right:", right_chars)
    #print("right bottom:", right_bot)

    for string, length in input_string_values.items():
        if length == 5 and sum([characters in right_bot for characters in string]) + \
                sum([characters in middle_char for characters in string]) + \
                sum([characters in top_char for characters in string]) == len(right_bot) + len(middle_char) + len(top_char):
            display_value[5] = [set(string), string]

    #print(display_value)
    print("display:", display)

    display_values = {}
    for j in range(0,len(display)):
        key = display[j]
        key_set = set(key)
        key_value = ''
        for k in range(0,len(display_value)):
            if display_value[k][0] == key_set:
                key_value = str(k)

            k += 1
        display_values[key] = [key_set, key_value]

    display_value_number = ''
    for each in display_values:
        display_value_number = display_value_number + display_values[each][1]

    print(display_value_number)
    #print("values:", display_values)
    #print("value:", display_value)
    #for each in display_values:


    #string = ''

    #for each in display_values:
    #    for k in range(0, len(display_value)):
    #        #print(each, k)
    #        if all([characters in display_value[k][0] for characters in each]) and len(each) == len(display_value[k][0]):
    #            #print("value:", display_value[k][0], "string:", string, "number", k)
    #            string = string + str(k)
    #print(string)
    #sum_values += int(string)
    #for string, length in display
    i += 1

#print(sum_values)


