def part_1(get_input):
    x = sum(int(item[1]) for item in get_input() if item[0] == "forward")
    y = sum(int(item[1]) for item in get_input() if item[0] == "down") - sum(
        int(item[1]) for item in get_input() if item[0] == "up"
    )

    answer = x * y

    return answer


def part_2(get_input):
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

    return answer
