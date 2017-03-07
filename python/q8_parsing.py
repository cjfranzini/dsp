#!/usr/bin/python
# -*- coding: utf-8 -*-

# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

def smallest_goal_difference():
    '''Reads a csv file of soccer stats and returns the name of the team with the smallest point differential
    '''
    
    with open('football.csv') as f:
        reader = csv.DictReader(f)

        smallest_diff = 100000000 # make initial comparison value unreasonably large
        team = None

        for row in reader:
            diff = int(row['Goals']) - int(row['Goals Allowed'])  
            diff = abs(diff) # absolute difference, comment for 'most-negative' difference ('Leicester', -34)

            if diff < smallest_diff:
                smallest_diff = diff
                team = row['Team']

    print (team, smallest_diff)

smallest_goal_difference()