from base_solver import BaseSolver


class Solver(BaseSolver):
    def part_one(self, puzzle_input) -> int:
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
        return self.totals[0]

    def part_two(self, puzzle_input) -> int:
        return sum(self.totals[0:3])
