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


def clean_data(input):
    for item in input:
        yield int(item)


def part_1(get_input):
    answer = sum(1 for _ in get_increases(clean_data(get_input())))
    return answer


def part_2(get_input):
    windows = get_windows(clean_data(get_input()))
    answer = sum(1 for _ in get_increases(windows))
    return answer
