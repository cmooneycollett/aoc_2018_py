"""
This module contains the runner methods used to run the AOC 2018 solution
functions and print out the results.
"""


def solve_day01():
    """
    Solves AOC 2018 Day 1 Parts 1 and 2, printing out the results.
    """
    print("AOC 2018 Day 1 - \"Chronal Calibration\"")
    input_data = day01.process_input_file()
    p1_solution = day01.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day01.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("============================================================")


def solve_day02():
    """
    Solves AOC 2018 Day 2 Parts 1 and 2, printing out the results.
    """
    print("AOC 2018 Day 2 - \"Inventory Management System\"")
    input_data = day02.process_input_file()
    p1_solution = day02.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day02.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("============================================================")


def solve_day03():
    """
    Solves AOC 2018 Day 3 Parts 1 and 2, printing out the results.
    """
    print("AOC 2018 Day 3 - \"No Matter How You Slice It\"")
    input_data = day03.process_input_file()
    p1_solution = day03.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day03.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("============================================================")


def solve_day04():
    """
    Solves AOC 2018 Day 4 Parts 1 and 2, printing out the results.
    """
    print("AOC 2018 Day 4 - \"Repose Record\"")
    input_data = day04.process_input_file()
    p1_solution = day04.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day04.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("============================================================")


def solve_day05():
    """
    Solves AOC 2018 Day 5 Parts 1 and 2, printing out the results.
    """
    print("AOC 2018 Day 5 - \"Alchemical Reduction\"")
    input_data = day05.process_input_file()
    p1_solution = day05.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day05.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("============================================================")


if __name__ == "__main__":
    # Import to allow execution from project top-level directory
    import os
    import sys
    sys.path.append(os.getcwd())
    # Solution module imports
    from src.solutions import day01, day02, day03, day04, day05
    # Main solver methods
    print("============================================================")
    solve_day01()
    solve_day02()
    solve_day03()
    solve_day04()
    solve_day05()
