

import random

from pprint import pprint


def pick_random(input_set, count=1):
    working_set = input_set.copy()
    try:
        items = random.sample(working_set, count)
    except ValueError:
        if len(working_set) > 0:
            items = random.sample(working_set, 1)
        else:
            return ([], set())

    for it in items:
        working_set.remove(it)

    return items, working_set


def combinations(input_set):
    # Get a matrix of all possible combinations
    output = [[] for x in range(1, len(input_set))]

    state = {}
    for item in input_set:
        nset = input_set.copy()
        nset.remove(item)
        state[item] = nset

    even = True
    if len(input_set) % 2:
        even = False

    if even:
        it_range = len(input_set) - 1
    else:
        it_range = len(input_set)

    # Keeps track of already left out items for odd input_set
    iteration_out = set()

    for it in range(0, it_range):
        print "START OUTSIDE ITERATION ------------- " + str(it)
        iteration_set = input_set.copy()
        if not even:
            for item in iteration_set:
                if item not in iteration_out:
                    iteration_out.add(item)
                    iteration_set.remove(item)
                    break

        while len(iteration_set) > 0:
            print "START INSIDE ITERATION ------------ "
            (litem, iteration_set) = pick_random(iteration_set, 1)
            #print litem, iteration_set
            available_teams = state[litem[0]].copy().intersection(iteration_set)
            #print "AVAILABLE TEAMS"
            #print available_teams
            (ritem, available_teams) = pick_random(available_teams, 1)
            #print "RITEM & ITERATION SET"
            #print ritem
            #print iteration_set
            iteration_set.remove(ritem[0])
            print " ------- RESULT :", litem[0], ritem[0], " -------- "
            state[litem[0]].remove(ritem[0])
            state[ritem[0]].remove(litem[0])
            #print "STATES"
            #print litem[0], state[litem[0]]
            #print ritem[0], state[ritem[0]]

















