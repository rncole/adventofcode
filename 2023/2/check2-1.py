#!/usr/bin/python
import string
# Advent of code 2022 challenge 2
import string as st
import functools

file = open('input', 'r')

roll_count = 0
rolls_count = 0
roll = []
i=0

bag_red = 12
bag_green = 13
bag_blue = 14
min_red = 0
min_green = 0
min_blue = 0
power = 0

games_possible = []
games_impossible = []

with (file as f):
    for line in f:
        roll = []
        cubes = []
        game, rolls = line.split(': ')
        game = int(game.split(' ')[1])
        rolls_count = rolls.count(';')+1
        rolls = rolls.strip()
        roll[roll_count:rolls_count] = rolls.split('; ')
        while i < rolls_count:
            roll[i] = roll[i].split(', ')
            i += 1
        for each in roll:
            for cubes in each:
                cubes = cubes.split(' ')
                if cubes[1] == 'red':
                    if int(cubes[0]) > min_red:
                        min_red = int(cubes[0])
                    if int(cubes[0]) <= bag_red:
                        games_possible.append(game) if game not in games_possible else games_possible
                    else:
                        games_impossible.append(game) if game not in games_impossible else games_impossible
                if cubes[1] == 'green':
                    if int(cubes[0]) > min_green:
                        min_green = int(cubes[0])
                    if int(cubes[0]) <= bag_green:
                        games_possible.append(game) if game not in games_possible else games_possible
                    else:
                        games_impossible.append(game) if game not in games_impossible else games_impossible
                if cubes[1] == 'blue':
                    if int(cubes[0]) > min_blue:
                        min_blue = int(cubes[0])
                    if int(cubes[0]) <= bag_blue:
                        games_possible.append(game) if game not in games_possible else games_possible
                    else:
                        games_impossible.append(game) if game not in games_impossible else games_impossible
        power = power + (min_red * min_green * min_blue)
        min_red = 0
        min_green = 0
        min_blue = 0
        i = 0
games_possible = [i for i in games_possible if i not in games_impossible]
print("Possible Games:", games_possible)
print("Impossible Games:", games_impossible)
print("Sum of Possible:", sum(games_possible))
print("Sum of the Power:", power)
