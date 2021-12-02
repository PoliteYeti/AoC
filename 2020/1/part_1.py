import os
from itertools import combinations
from functools import reduce


def get_input():
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(filepath, "r") as input_file:
        for line in input_file:
            yield int(line)


combos = combinations(get_input(), 2)

for combo in combos:
    if sum(combo) == 2020:
        print(reduce(lambda x, y: x * y, combo))
        break
