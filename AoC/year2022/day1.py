from AoC.base_solver import BaseSolver


class Solver(BaseSolver):
    def part_one(self, puzzle_input) -> str:
        self.totals = []
        total = 0

        for line in puzzle_input:
            if line == b"":
                self.totals.append(total)
                total = 0
            else:
                total += int(line)

        self.totals.append(total)
        self.totals.sort(reverse=True)
        return str(self.totals[0])

    def part_two(self, puzzle_input) -> str:
        return str(sum(self.totals[0:3]))
