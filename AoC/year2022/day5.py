from AoC.base_solver import BaseSolver


class Solver(BaseSolver):
    def build_stacks(self, puzzle_input):
        parsed_lines = []
        stacks = {}

        for line in puzzle_input:
            if line == b"":
                break

            parsed_lines.insert(0, line.decode("UTF-8"))

        labels = parsed_lines[0]

        for index, value in enumerate(labels):
            if value.isnumeric():
                stacks[value] = []
                for line in parsed_lines[1:]:
                    if line[index].isalpha():
                        stacks[value].append(line[index])
        return stacks

    def get_result(self, stacks):
        result = []

        for i in range(len(stacks)):
            result.append(stacks[str(i + 1)][-1])

        return "".join(result)

    def part_one(self, puzzle_input) -> str:
        stacks = self.build_stacks(puzzle_input)

        for line in puzzle_input:
            loop, src, dest = [
                itm for itm in line.decode("UTF-8").split() if itm.isnumeric()
            ]
            for _ in range(int(loop)):
                crate = stacks[src].pop()
                stacks[dest].append(crate)

        return self.get_result(stacks)

    def part_two(self, puzzle_input) -> str:
        stacks = self.build_stacks(puzzle_input)

        cratestack = []

        for line in puzzle_input:
            loop, src, dest = [
                itm for itm in line.decode("UTF-8").split() if itm.isnumeric()
            ]

            for _ in range(int(loop)):
                cratestack.append(stacks[src].pop())

            for _ in range(int(loop)):
                stacks[dest].append(cratestack.pop())

        return self.get_result(stacks)
