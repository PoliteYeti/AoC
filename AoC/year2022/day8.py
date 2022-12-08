from AoC.base_solver import BaseSolver


class Solver(BaseSolver):
    def part_one(self, puzzle_input) -> str:
        rows = []
        for line in puzzle_input:
            rows.append(line.decode('UTF-8'))
        
        WIDTH = len(rows[0])
        HEIGHT = len(rows)

        visible = WIDTH * 2 + HEIGHT * 2 - 4
        
        for y, row in enumerate(rows[1:-1]):
            for x, position in enumerate(row[1:-1]):

                print(x, y)

    def part_two(self, puzzle_input) -> str:
        pass
