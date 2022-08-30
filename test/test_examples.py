"""
This module contains additional test methods used to test AOC 2018 solutions
against example inputs. This test module is configured to use the pytest
library.
"""

from src.solutions import day08


def test_day08_part1():
    """
    Solution test method for AOC 2018 Day 8 Part 1.
    """
    input_data = day08.process_input_file(
        filepath="./input/example/day08_ex01.txt")
    solution = day08.solve_part1(input_data)
    assert solution == 138


def test_day08_part2():
    """
    Solution test method for AOC 2018 Day 8 Part 2.
    """
    input_data = day08.process_input_file(
        filepath="./input/example/day08_ex01.txt")
    solution = day08.solve_part2(input_data)
    assert solution == 66
