"""
Solutions for AOC 2018 Day 2 - "Inventory Management System".
"""

from collections import Counter


def process_input_file(filepath="./input/day02.txt"):
    """
    Processes the AOC 2018 Day 2 input file into the format required by the
    solver functions. Returns the list of strings given in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()
                if len(line.strip()) > 0]


def solve_part1(box_codes):
    """
    Solves AOC 2018 Day 2 Part 1 // Returns the checksum of the list of box
    codes, which is the product of the counts of codes with two and three of
    any letter.
    """
    count_two = 0
    count_three = 0
    for code in box_codes:
        letter_counts = Counter(code)
        if 2 in letter_counts.values():
            count_two += 1
        if 3 in letter_counts.values():
            count_three += 1
    return count_two * count_three


def solve_part2(_box_codes):
    """
    Solves AOC 2018 Day 2 Part 2 // ###
    """
    return NotImplemented
