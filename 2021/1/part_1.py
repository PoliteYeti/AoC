import os


def get_input():
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(filepath, "r") as input_file:
        for line in input_file:
            yield int(line)


def get_increases(items):
    last_item = None
    for current_item in items:

        if not last_item:
            last_item = current_item

        if current_item > last_item:
            yield current_item
        last_item = current_item


answer = sum(1 for _ in get_increases(get_input()))

print(answer)
