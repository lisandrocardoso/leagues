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

