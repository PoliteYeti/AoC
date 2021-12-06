def make_boards(input):
    M = []
    for item in input:
        if len(item.strip()) > 0:
            M.append([int(number) for number in item.split()])
        else:
            yield M
            M = []
    yield M


def play_board(input_numbers, board):
    called_nums = set()
    for index, number in enumerate(input_numbers):

        def get_score(board):
            all_board_nums = {item for row in board for item in row}
            return sum(num for num in all_board_nums.difference(called_nums)) * number

        called_nums.add(number)

        for row in board:
            if called_nums.issuperset(set(row)):
                return index, get_score(board)

        t_board = [[row[i] for row in board] for i in range(len(board))]

        for row in t_board:
            if called_nums.issuperset(set(row)):
                return index, get_score(t_board)


def part_1(get_input):
    lines = get_input()

    input_numbers = [int(number) for number in next(lines).split(",")]
    next(lines)

    boards = [board for board in make_boards(lines)]

    results = [play_board(input_numbers, board) for board in boards]
    results.sort(key=lambda x: x[0])
    return results[0][1]


def part_2(get_input):
    lines = get_input()

    input_numbers = [int(number) for number in next(lines).split(",")]
    next(lines)

    boards = [board for board in make_boards(lines)]

    results = [play_board(input_numbers, board) for board in boards]
    results.sort(key=lambda x: x[0], reverse=True)
    return results[0][1]
