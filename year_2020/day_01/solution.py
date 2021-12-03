from itertools import combinations
from functools import reduce


def clean_data(data):
    for item in data:
        yield int(item[0])


def part_1(get_input):
    combos = combinations(clean_data(get_input()), 2)

    for combo in combos:
        if sum(combo) == 2020:
            answer = reduce(lambda x, y: x * y, combo)
            break

    return answer


def part_2(get_input):
    combos = combinations(clean_data(get_input()), 3)

    for combo in combos:
        if sum(combo) == 2020:
            answer = reduce(lambda x, y: x * y, combo)
            break

    return answer
