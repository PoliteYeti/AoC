import os
from importlib import import_module

import requests
from dotenv import load_dotenv

YEAR = 2022
DAY = 5


def puzzle_input(year: int, day: int):

    cookies = {
        "session": os.environ["SESSION"],
    }

    response = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{DAY}/input", cookies=cookies
    )
    for line in response.iter_lines():
        yield line


if __name__ == "__main__":
    load_dotenv()
    solver = import_module(f"year{YEAR}.day{DAY}").Solver()

    print(f"Answer 1: {solver.part_one(puzzle_input(YEAR,DAY))}")
    print(f"Answer 2: {solver.part_two(puzzle_input(YEAR,DAY))}")
