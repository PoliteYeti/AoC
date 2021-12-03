import importlib
import os

from utils import get_input_factory

YEAR = "2021"
DAY = "03"


def run_puzzle(year, day):
    solution = importlib.import_module(f"year_{year}.day_{day}.solution")

    input_file_path = os.path.join(
        os.path.dirname(__file__), f"year_{year}", f"day_{day}", "input.txt"
    )

    get_input = get_input_factory(input_file_path)

    solution_1 = solution.part_1(get_input)
    solution_2 = solution.part_2(get_input)

    print(f"{YEAR}, Day {DAY}, Part 1 solution is: {solution_1}")
    print(f"{YEAR}, Day {DAY}, Part 2 solution is: {solution_2}")


if __name__ == "__main__":
    run_puzzle(YEAR, DAY)
