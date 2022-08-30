"""
This module contains the test methods used to test the AOC 2018 solutions
against the actual problem input files. This test module is configured to use
the pytest library.
"""

from src.solutions import day01, day02, day03, day04, day05, day06, day07, \
    day08


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


def test_day02_part1():
    """
    Solution test method for AOC 2018 Day 2 Part 1.
    """
    input_data = day02.process_input_file()
    solution = day02.solve_part1(input_data)
    assert solution == 5478


def test_day02_part2():
    """
    Solution test method for AOC 2018 Day 2 Part 2.
    """
    input_data = day02.process_input_file()
    solution = day02.solve_part2(input_data)
    assert solution == "qyzphxoiseldjrntfygvdmanu"


def test_day03_part1():
    """
    Solution test method for AOC 2018 Day 3 Part 1.
    """
    input_data = day03.process_input_file()
    solution = day03.solve_part1(input_data)
    assert solution == 121163


def test_day03_part2():
    """
    Solution test method for AOC 2018 Day 3 Part 2.
    """
    input_data = day03.process_input_file()
    solution = day03.solve_part2(input_data)
    assert solution == 943


def test_day04_part1():
    """
    Solution test method for AOC 2018 Day 4 Part 1.
    """
    input_data = day04.process_input_file()
    solution = day04.solve_part1(input_data)
    assert solution == 94040


def test_day04_part2():
    """
    Solution test method for AOC 2018 Day 4 Part 2.
    """
    input_data = day04.process_input_file()
    solution = day04.solve_part2(input_data)
    assert solution == 39940


def test_day05_part1():
    """
    Solution test method for AOC 2018 Day 5 Part 1.
    """
    input_data = day05.process_input_file()
    solution = day05.solve_part1(input_data)
    assert solution == 10878


def test_day05_part2():
    """
    Solution test method for AOC 2018 Day 5 Part 2.
    """
    input_data = day05.process_input_file()
    solution = day05.solve_part2(input_data)
    assert solution == 6874


def test_day06_part1():
    """
    Solution test method for AOC 2018 Day 6 Part 1.
    """
    input_data = day06.process_input_file()
    solution = day06.solve_part1(input_data)
    assert solution == 5941


def test_day06_part2():
    """
    Solution test method for AOC 2018 Day 6 Part 2.
    """
    input_data = day06.process_input_file()
    solution = day06.solve_part2(input_data)
    assert solution == 40244


def test_day07_part1():
    """
    Solution test method for AOC 2018 Day 7 Part 1.
    """
    input_data = day07.process_input_file()
    solution = day07.solve_part1(input_data)
    assert solution == "IJLFUVDACEHGRZPNKQWSBTMXOY"


def test_day07_part2():
    """
    Solution test method for AOC 2018 Day 7 Part 2.
    """
    input_data = day07.process_input_file()
    solution = day07.solve_part2(input_data)
    assert solution == 1072


def test_day08_part1():
    """
    Solution test method for AOC 2018 Day 8 Part 1.
    """
    input_data = day08.process_input_file()
    solution = day08.solve_part1(input_data)
    assert solution == 42254


def test_day08_part2():
    """
    Solution test method for AOC 2018 Day 8 Part 2.
    """
    input_data = day08.process_input_file()
    solution = day08.solve_part2(input_data)
    assert solution == 25007
