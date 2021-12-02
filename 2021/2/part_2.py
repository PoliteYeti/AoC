import os


def get_input():
    with open(os.path.join(os.path.dirname(__file__), "input.txt"), "r") as input_file:
        for line in input_file:
            yield line.split()


x = y = a = 0

for direction in get_input():
    if direction[0] in ["up", "down"]:
        aim_adjust = (
            int(direction[1])
            if direction[0] == "down"
            else -int(direction[1])
            if direction[0] == "up"
            else 0
        )
        a += aim_adjust
    else:
        x, y = x + int(direction[1]), y + a * int(direction[1])

answer = x * y

print(answer)
