"""
Solutions for AOC 2018 Day 1 - "Chronal Calibration".
"""


def process_input_file(filepath="./input/day01.txt"):
    """
    Processes the AOC 2018 Day 1 input file into the format required by the
    solver functions. Returns list of integer values listed in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return [int(line.strip()) for line in file.readlines()
                if len(line.strip()) > 0]


def solve_part1(frequency_deltas):
    """
    Solves AOC 2018 Day 1 Part 1 // Returns the resulting frequency after all of
    the changes in frequency are applied, from a starting frequency of 0.
    """
    return sum(frequency_deltas)


def solve_part2(_frequency_deltas):
    """
    Solves AOC 2018 Day 1 Part 2 // ###
    """
    return NotImplemented
