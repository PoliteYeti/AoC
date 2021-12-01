import os

input_list = []

with open(f'{os.path.dirname(__file__)}\\input.txt', 'r') as input_file:
    for line in input_file:
        input_list.append(int(line))

def get_increases(items):
    last_item = items[0]
    for current_item in items:
        if current_item > last_item:
            yield current_item
        last_item = current_item

increases = [item for item in get_increases(input_list)]

print(len(increases))