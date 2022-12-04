#!/usr/bin/python


# Advent of code 2022 challenge 2
import string as st
import functools

file = open('input', 'r')

line = 0
rules_scores = [('Rock', 'Scissors', 1, 'A', 'C', 'B'), ('Scissors', 'Paper', 3, 'C', 'B', 'A'), ('Paper', 'Rock', 2, 'B', 'A', 'C')]
x = 0
score = 0
wins = 0

with file as f:
    for line in f:
        print("\n")
        opp_throw = line.partition(' ')[0].strip()
        throw = line.partition(' ')[2].strip()
        if throw == "X":
            print("Need to Lose")

        if throw == "Y":
            print("Need to Draw")
            throw = opp_throw

        if throw == "Z":
            print("Need to Win")

        for each in rules_scores:
            if opp_throw == each[3]:
                opp_throw = each[0]
                if throw == "X":
                    throw = each[4]
                if throw == "Z":
                    throw = each[5]
        for each in rules_scores:
            if throw == each[3]:
                throw = each[0]
                score_throw = each[2]
                beats = each[1]
            x += 1
        x = 0
        print("Your Opponent threw", opp_throw, "and you threw", throw)
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


