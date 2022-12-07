from abc import ABC, abstractmethod
from typing import Callable


class BaseSolver(ABC):
    @abstractmethod
    def part_one(self, puzzle_input: Callable) -> str:
        ...

    @abstractmethod
    def part_two(self, puzzle_input: Callable) -> str:
        ...
