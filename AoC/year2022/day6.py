from base_solver import BaseSolver


class Solver(BaseSolver):
    def get_packet_marker(self, buffer: str, packet_len: int) -> int:
        for i, _ in enumerate(buffer):
            candidate = buffer[i : i + packet_len]
            charset = set(candidate)
            if len(charset) == packet_len:
                return i + packet_len

    def part_one(self, puzzle_input) -> int:
        buffer = next(puzzle_input).decode("UTF-8")

        return self.get_packet_marker(buffer, 4)

    def part_two(self, puzzle_input) -> int:
        buffer = next(puzzle_input).decode("UTF-8")

        return self.get_packet_marker(buffer, 14)
