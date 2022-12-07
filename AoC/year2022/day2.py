from AoC.base_solver import BaseSolver


class Solver(BaseSolver):
    def __init__(self) -> None:
        self.scoremap = {
            b"A X": [1 + 3, 0 + 3],
            b"A Y": [2 + 6, 3 + 1],
            b"A Z": [3 + 0, 6 + 2],
            b"B X": [1 + 0, 0 + 1],
            b"B Y": [2 + 3, 3 + 2],
            b"B Z": [3 + 6, 6 + 3],
            b"C X": [1 + 6, 0 + 2],
            b"C Y": [2 + 0, 3 + 3],
            b"C Z": [3 + 3, 6 + 1],
        }

    def part_one(self, puzzle_input) -> str:
        score = 0
        for line in puzzle_input:
            score += self.scoremap[line][0]
        return str(score)

    def part_two(self, puzzle_input) -> str:
        score = 0
        for line in puzzle_input:
            score += self.scoremap[line][1]
        return str(score)
