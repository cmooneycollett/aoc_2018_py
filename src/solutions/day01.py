"""
Solutions for AOC 2018 Day 1 - "Chronal Calibration".
"""

import itertools


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


def solve_part2(frequency_deltas):
    """
    Solves AOC 2018 Day 1 Part 2 // Returns the first frequency that is reached
    twice, from a starting frequency of 0 and using the given frequency deltas.
    """
    frequency = 0
    seen = set([frequency])
    for delta in itertools.cycle(frequency_deltas):
        frequency += delta
        if frequency in seen:
            return frequency
        seen.add(frequency)
    raise RuntimeError("AOC 2018 D1-P2: did not observe a single frequency "
                       "value twice")
