import argparse
import importlib
import os

from utils import get_input_factory

YEAR = 2021
DAY = 3


def run_puzzle(year, day):
    solution = importlib.import_module(f"year_{year}.day_{day:02}.solution")

    input_file_path = os.path.join(
        os.path.dirname(__file__), f"year_{year}", f"day_{day:02}", "input.txt"
    )

    get_input = get_input_factory(input_file_path)

    solution_1 = solution.part_1(get_input)
    solution_2 = solution.part_2(get_input)

    print(f"{year}, Day {day:02}, Part 1 solution is: {solution_1}")
    print(f"{year}, Day {day:02}, Part 2 solution is: {solution_2}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="AoC Runner",
        description="Handy dandy util for executing puzzle solutions.",
    )
    parser.add_argument("--day", action="store", default=DAY, type=int)
    parser.add_argument("--year", action="store", default=YEAR, type=int)

    arguments = parser.parse_args()

    run_puzzle(arguments.year, arguments.day)
