

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
    def shift_right(input_list):
        working_list = input_list
        first = working_list[0]
        working_list.remove(first)
        carry = working_list[0]
        working_list.remove(carry)
        working_list.append(carry)
        working_list.insert(0, first)
        return working_list

    def reverse(input_list):
        return input_list[::-1]

    output_list = []

    a_list = []

    for item in input_set:
        a_list.append(item)

    b_list = reverse(a_list)

    for it in range(0, len(input_set) - 1):
        output_list.append([])
        for idx in range(0, len(input_set) / 2):
            output_list[it].append([a_list[idx], b_list[idx]])
        a_list = shift_right(a_list)
        b_list = reverse(a_list)

    return output_list


