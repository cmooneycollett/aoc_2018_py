"""
This module contains the test methods used to test the AOC 2018 solutions
against the actual problem input files. This test module is configured to use
the pytest library.
"""

from src.solutions import day01


def test_day01_part1():
    """
    Solution test method for AOC 2018 Day 1 Part 1.
    """
    input_data = day01.process_input_file()
    solution = day01.solve_part1(input_data)
    assert solution == 466


def test_day01_part2():
    """
    Solution test method for AOC 2018 Day 1 Part 2.
    """
    input_data = day01.process_input_file()
    solution = day01.solve_part2(input_data)
    assert solution == 750
