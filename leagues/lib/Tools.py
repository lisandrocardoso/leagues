import random

def pick_random(input_set, count = 1):
    try:
        items = random.sample(input_set, count)
    except ValueError:
        if len(input_set) > 0:
            items = random.sample(input_set, 1)
        else:
            return ([], set())

    for it in items:
        input_set.remove(it)

    return items, input_set

# Get a matrix of all possible combinations
def combinations(input_set):
    output = []
    for i in range(0, len(input_set)):
        (id, result_set) = pick_random(input_set)
            for j in 




