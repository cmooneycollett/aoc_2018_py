"""
This module contains the test methods used to test the AOC 2018 solutions
against the actual problem input files. This test module is configured to use
the pytest library.
"""

from src.solutions import day01, day02, day03, day04, day05, day06, day07, \
    day08, day09, day10, day11, day12, day13, day14


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


def test_day09_part1():
    """
    Solution test method for AOC 2018 Day 9 Part 1.
    """
    input_data = day09.process_input_file()
    solution = day09.solve_part1(input_data)
    assert solution == 412127


def test_day09_part2():
    """
    Solution test method for AOC 2018 Day 9 Part 2.
    """
    input_data = day09.process_input_file()
    solution = day09.solve_part2(input_data)
    assert solution == 3482394794


def test_day10_part1():
    """
    Solution test method for AOC 2018 Day 10 Part 1.
    """
    input_data = day10.process_input_file()
    solution = day10.solve_part1(input_data)
    assert solution == "XLZAKBGZ"


def test_day10_part2():
    """
    Solution test method for AOC 2018 Day 10 Part 2.
    """
    input_data = day10.process_input_file()
    solution = day10.solve_part2(input_data)
    assert solution == 10656


def test_day11_part1():
    """
    Solution test method for AOC 2018 Day 11 Part 1.
    """
    input_data = day11.process_input_file()
    solution = day11.solve_part1(input_data)
    assert solution == "21,34"


def test_day11_part2():
    """
    Solution test method for AOC 2018 Day 11 Part 2.
    """
    input_data = day11.process_input_file()
    solution = day11.solve_part2(input_data)
    assert solution == "90,244,16"


def test_day12_part1():
    """
    Solution test method for AOC 2018 Day 12 Part 1.
    """
    input_data = day12.process_input_file()
    solution = day12.solve_part1(input_data)
    assert solution == 3890


def test_day12_part2():
    """
    Solution test method for AOC 2018 Day 12 Part 2.
    """
    input_data = day12.process_input_file()
    solution = day12.solve_part2(input_data)
    assert solution == 4800000001087


def test_day13_part1():
    """
    Solution test method for AOC 2018 Day 13 Part 1.
    """
    input_data = day13.process_input_file()
    solution = day13.solve_part1(input_data)
    assert solution == "8,9"


def test_day13_part2():
    """
    Solution test method for AOC 2018 Day 13 Part 2.
    """
    input_data = day13.process_input_file()
    solution = day13.solve_part2(input_data)
    assert solution == "73,33"


def test_day14_part1():
    """
    Solution test method for AOC 2018 Day 14 Part 1.
    """
    input_data = day14.process_input_file()
    solution = day14.solve_part1(input_data)
    assert solution == "6289129761"


def test_day14_part2():
    """
    Solution test method for AOC 2018 Day 14 Part 2.
    """
    input_data = day14.process_input_file()
    solution = day14.solve_part2(input_data)
    assert solution == 20207075
