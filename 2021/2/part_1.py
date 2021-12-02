import os

def get_input():
    with open(f'{os.path.dirname(__file__)}\\input.txt', 'r') as input_file:
        for line in input_file:
            yield line.split()
x = y = 0

x = sum(int(item[1]) for item in get_input() if item[0] == 'forward')
y = sum(int(item[1]) for item in get_input() if item[0] == 'down') + sum(-int(item[1]) for item in get_input() if item[0] == 'up')

answer = x*y

print(answer)