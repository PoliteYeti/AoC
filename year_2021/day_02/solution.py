def clean_data(input):
    for item in input:
        item = item.split()
        yield (str(item[0]), int(item[1]))


def part_1(get_input):
    x = sum(item[1] for item in clean_data(get_input()) if item[0] == "forward")
    downs = sum(item[1] for item in clean_data(get_input()) if item[0] == "down")
    ups = sum(item[1] for item in clean_data(get_input()) if item[0] == "up")

    answer = x * (downs - ups)

    return answer


def part_2(get_input):
    x = y = a = 0

    for instruction in clean_data(get_input()):
        direction = instruction[0]
        magnitude = instruction[1]
        if direction in ["up", "down"]:
            aim_adjust = magnitude if direction == "down" else -magnitude
            a += aim_adjust
        else:
            x, y = x + magnitude, y + a * magnitude

    answer = x * y

    return answer
