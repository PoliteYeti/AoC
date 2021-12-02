import os


def get_input():
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(filepath, "r") as input_file:
        for line in input_file:
            yield line.split()


x = y = a = 0

for instruction in get_input():
    direction = instruction[0]
    magnitude = int(instruction[1])
    if direction in ["up", "down"]:
        aim_adjust = magnitude if direction == "down" else -magnitude
        a += aim_adjust
    else:
        x, y = x + magnitude, y + a * magnitude

answer = x * y

print(answer)
