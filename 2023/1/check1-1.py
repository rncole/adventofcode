#!/usr/bin/python

# Advent of code 2023 challenge 1

file = open('input', 'r')

line = ""
char = ""
line_cal_v = ""
cal_value = []
line_num = 0
char_check = 0
first_digit = ""
last_digit = ""
line_str = ""

def words2nums(line_str):
    line_str = line_str.replace("one", "1")
    line_str = line_str.replace("two", "2")
    line_str = line_str.replace("three", "3")
    line_str = line_str.replace("four", "4")
    line_str = line_str.replace("five", "5")
    line_str = line_str.replace("six", "6")
    line_str = line_str.replace("seven", "7")
    line_str = line_str.replace("eight", "8")
    line_str = line_str.replace("nine", "9")
    return line_str

with file as f:
    for line in f:
#        print("Input:", line.strip())
        line = line.strip()
        for char in line:
            line_str = line_str + char
            # Uncomment the next line for part 2 solution
            line_str = words2nums(line_str)
        for char in line_str:
            char = str(char)
            if(char.isnumeric()):
                #print("number!")
                first_digit = char
                break
        line_str = ""
        line_inv = line[::-1]
        for char in line_inv:
            line_str = char + line_str
            # Uncomment the next line for part 2 solution
            line_str = words2nums(line_str)
            #print(line_str)
        for char in line_str[::-1]:
            char = str(char)
            if(char.isnumeric()):
                #print("number!")
                last_digit = char
                break
        line_str = ""
#        print("First Digit: ", first_digit)
#        print("Last Digit: ", last_digit)

        line_cal_v = str(first_digit) + str(last_digit)
#       print("Cal: ", line_cal_v)
        cal_value.append(int(line_cal_v))
        line_num += 1
        char_check = 0
        first_digit = ""
        last_digit = ""
    print("Calibration Sum:", sum(cal_value))
