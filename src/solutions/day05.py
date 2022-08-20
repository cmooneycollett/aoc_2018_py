"""
Solutions for AOC 2018 Day 5 - "Alchemical Reduction".
"""

import re
import string


def process_input_file(filepath="./input/day05.txt"):
    """
    Processes the AOC 2018 Day 5 input file into the format required by the
    solver functions. Returns the polymer string given in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(polymer: str):
    """
    Solves AOC 2018 Day 5 Part 1 // Returns the length of the polymer resulting
    from reacting the given polymer.
    """
    new_polymer = react_polymer(polymer)
    return len(new_polymer)


def solve_part2(polymer: str):
    """
    Solves AOC 2018 Day 5 Part 2 // Returns the length of the shortest polymer
    resulting from fully removing all of one type of unit and reacting the
    improved polymer.
    """
    min_length = None
    for char in string.ascii_lowercase:
        # Improve polymer by removing all of a single type of unit
        improved_polymer = re.sub(fr"({char}|{char.upper()})", "", polymer)
        # Fully react the improved polymer and check if it is the shortest so far
        reacted_polymer = react_polymer(improved_polymer)
        if min_length is None or len(reacted_polymer) < min_length:
            min_length = len(reacted_polymer)
    return min_length


def react_polymer(polymer: str):
    """
    Reacts the given polymer, returning the resulting polymer.
    """
    new_polymer = str(polymer)
    while True:
        no_reaction = True
        for char in string.ascii_lowercase:
            old_len = len(new_polymer)
            # Remove unit pairs of same type and different polarity
            new_polymer = new_polymer.replace(f"{char}{char.upper()}", "")
            new_polymer = new_polymer.replace(f"{char.upper()}{char}", "")
            # Check if reaction occured
            if old_len > len(new_polymer):
                no_reaction = False
        if no_reaction:
            break
    return new_polymer
