from itertools import product, repeat

def build_lines(get_input, filter_diags=True):
    for input in get_input():
        coords = input.split("->")
        x1, y1, x2, y2 = (
            int(dimension) for coord in coords for dimension in coord.split(",")
        )
        line = (x1, y1, x2, y2)

        if filter_diags and x1 != x2 and y1 != y2:
            continue

        yield line


def expand_line(line):
    x1, y1, x2, y2 = (item for item in line)
    
    x_direction = -1 if x1 > x2 else 1
    y_direction = -1 if y1 > y2 else 1 

    x_iter = repeat(x1) if x1 == x2 else range(x1, x2+x_direction, x_direction)
    y_iter = repeat(y1) if y1 == y2 else range(y1, y2+y_direction, y_direction)

    for item in zip(x_iter, y_iter):
        yield item

def mark_map(coord, line_map):
    x, y = coord[0], coord[1]
    line_map[x] = line_map.get(x, {})
    line_map[x][y] = line_map[x].get(y, 0) + 1

    return line_map


def get_intersections(get_input, filter_diags=True):
    line_map = {}
    for line in build_lines(get_input, filter_diags=filter_diags):
        for coord in expand_line(line):
            line_map = mark_map(coord, line_map)

    intersections = sum(
        [
            1
            for col in line_map.keys()
            for row in line_map[col].keys()
            if line_map[col][row] > 1
        ]
    )

    return intersections


def part_1(get_input):
    return get_intersections(get_input, filter_diags=True)


def part_2(get_input):
    return get_intersections(get_input, filter_diags=False)
