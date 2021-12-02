import os


def get_input():
    filepath = os.path.join(os.path.dirname(__file__), "input.txt")
    with open(filepath, "r") as input_file:
        for line in input_file:
            yield line.split()


x = sum(int(item[1]) for item in get_input() if item[0] == "forward")
y = sum(int(item[1]) for item in get_input() if item[0] == "down") - sum(
    int(item[1]) for item in get_input() if item[0] == "up"
)

answer = x * y

print(answer)
