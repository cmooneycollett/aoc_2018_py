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


def solve_part2(box_codes):
    """
    Solves AOC 2018 Day 2 Part 2 // Determines the letters that are common
    between the two box codes that differ by only a single letter.
    """
    for (index_i, code) in enumerate(box_codes):
        for index_j in range(index_i + 1, len(box_codes)):
            mismatch_letters = ""
            for (index_char, char) in enumerate(code):
                if char != box_codes[index_j][index_char]:
                    mismatch_letters += char
                    if len(mismatch_letters) > 1:
                        break
            if len(mismatch_letters) == 1:
                return code.replace(mismatch_letters, "")
    raise RuntimeError("AOC 2018 D2-P2: did not find the two correct box IDs!")
