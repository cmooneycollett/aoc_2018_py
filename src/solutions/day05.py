"""
Solutions for AOC 2018 Day 5 - "Alchemical Reduction".
"""

import string


def process_input_file(filepath="./input/day05.txt"):
    """
    Processes the AOC 2018 Day 5 input file into the format required by the
    solver functions. Returns the polymer string given in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(polymer):
    """
    Solves AOC 2018 Day 5 Part 1 // Returns the length of the polymer resulting
    from reacting the given polymer.
    """
    new_polymer = react_polymer(polymer)
    return len(new_polymer)


def solve_part2(_polymer):
    """
    Solves AOC 2018 Day 5 Part 2 // ###
    """
    return NotImplemented


def react_polymer(polymer):
    """
    Reacts the given polymer, returning the resulting polymer.
    """
    pairs = []
    for char in string.ascii_lowercase:
        pairs.append(f"{char}{char.upper()}")
        pairs.append(f"{char.upper()}{char}")
    new_polymer = str(polymer)
    while True:
        no_reaction = True
        for pair in pairs:
            old_len = len(new_polymer)
            new_polymer = new_polymer.replace(pair, "")
            if old_len > len(new_polymer):
                no_reaction = False
        if no_reaction:
            break
    return new_polymer
