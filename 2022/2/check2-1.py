#!/usr/bin/python


# Advent of code 2022 challenge 2
import string as st
import functools

file = open('input', 'r')

line = 0
rules_scores = [('Rock', 'Scissors', 1, 'A', 'X'), ('Scissors', 'Paper', 3, 'C', 'Z'), ('Paper', 'Rock', 2, 'B', 'Y')]
x = 0
score = 0
wins = 0

with file as f:
    for line in f:
        opp_throw = line.partition(' ')[0].strip()
        throw = line.partition(' ')[2].strip()
        for each in rules_scores:
            if opp_throw == each[3]:
                opp_throw = each[0]
            if throw == each[4]:
                throw = each[0]
                score_throw = each[2]
                beats = each[1]
            x += 1
        x = 0
        print("\nYour Opponent threw", opp_throw, "and you threw", throw)
        if beats == opp_throw:
            print("You Won!")
            score += (6 + score_throw)
            wins += 1
        elif throw == opp_throw:
            print("Draw!")
            score += (3 + score_throw)
        else:
            print("You Lost!")
            score += score_throw

print("\nYou won", wins, "times for a total score of", score)


