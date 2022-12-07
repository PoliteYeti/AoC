from base_solver import BaseSolver


class Solver(BaseSolver):
    def _prep_input(self, line):
        pairs = line.decode("UTF-8").split(",")
        start1, end1 = pairs[0].split("-")
        start2, end2 = pairs[1].split("-")

        set1 = set(range(int(start1), int(end1) + 1))
        set2 = set(range(int(start2), int(end2) + 1))

        return set1, set2

    def part_one(self, puzzle_input) -> int:
        overlaps = 0
        for line in puzzle_input:
            set1, set2 = self._prep_input(line)

            if set1.issuperset(set2) or set2.issuperset(set1):
                overlaps += 1

        return overlaps

    def part_two(self, puzzle_input) -> int:
        overlaps = 0
        for line in puzzle_input:
            set1, set2 = self._prep_input(line)

            if len(set1.intersection(set2)) > 0:
                overlaps += 1

        return overlaps
