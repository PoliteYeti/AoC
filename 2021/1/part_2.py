import os

def get_input():
    with open(f'{os.path.dirname(__file__)}\\input.txt', 'r') as input_file:
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

def get_windows(items):
    window = []
    for item in items:
        window.append(item)
        if len(window) > 2:
            yield sum(window)
            window.pop(0)


windows = (item for item in get_windows(get_input()))

increases = [item for item in get_increases(windows)]

print(len(increases))