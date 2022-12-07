from AoC.base_solver import BaseSolver


class Solver(BaseSolver):
    def part_one(self, puzzle_input) -> str:
        priority = 0
        for line in puzzle_input:
            compartment1 = set(line[0 : len(line) // 2])
            compartment2 = set(line[len(line) // 2 :])
            result = set.intersection(compartment1, compartment2).pop()
            result = result - 96 if result > 96 else result - 38

            priority += result
        return str(priority)

    def part_two(self, puzzle_input) -> str:
        group = []
        priority = 0

        for line in puzzle_input:
            group.append(line)
            if len(group) == 3:
                result = set.intersection(
                    set(group[0]), set(group[1]), set(group[2])
                ).pop()
                result = result - 96 if result > 96 else result - 38
                group = []

                priority += result
        return str(priority)
