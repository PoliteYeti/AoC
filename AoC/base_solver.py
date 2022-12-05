from abc import ABC, abstractmethod


class BaseSolver(ABC):
    @abstractmethod
    def part_one(puzzle_input: callable):
        ...

    @abstractmethod
    def part_two(puzzle_input: callable):
        ...
