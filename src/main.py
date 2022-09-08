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


def solve_day06():
    """
    Solves AOC 2018 Day 6 Parts 1 and 2, printing out the results.
    """
    print("AOC 2018 Day 6 - \"Chronal Coordinates\"")
    input_data = day06.process_input_file()
    p1_solution = day06.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day06.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("============================================================")


def solve_day07():
    """
    Solves AOC 2018 Day 7 Parts 1 and 2, printing out the results.
    """
    print("AOC 2018 Day 7 - \"The Sum of Its Parts\"")
    input_data = day07.process_input_file()
    p1_solution = day07.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day07.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("============================================================")


def solve_day08():
    """
    Solves AOC 2018 Day 8 Parts 1 and 2, printing out the results.
    """
    print("AOC 2018 Day 8 - \"Memory Maneuver\"")
    input_data = day08.process_input_file()
    p1_solution = day08.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day08.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("============================================================")


def solve_day09():
    """
    Solves AOC 2018 Day 9 Parts 1 and 2, printing out the results.
    """
    print("AOC 2018 Day 9 - \"Marble Mania\"")
    input_data = day09.process_input_file()
    p1_solution = day09.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day09.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("============================================================")


def solve_day10():
    """
    Solves AOC 2018 Day 10 Parts 1 and 2, printing out the results.
    """
    print("AOC 2018 Day 10 - \"The Stars Align\"")
    input_data = day10.process_input_file()
    p1_solution = day10.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day10.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("============================================================")


def solve_day11():
    """
    Solves AOC 2018 Day 11 Parts 1 and 2, printing out the results.
    """
    print("AOC 2018 Day 11 - \"Chronal Charge\"")
    input_data = day11.process_input_file()
    p1_solution = day11.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day11.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("============================================================")


if __name__ == "__main__":
    # Import to allow execution from project top-level directory
    import os
    import sys
    sys.path.append(os.getcwd())
    # Solution module imports
    from src.solutions import day01, day02, day03, day04, day05, day06, day07, \
        day08, day09, day10, day11
    # Main solver methods
    print("============================================================")
    solve_day01()
    solve_day02()
    solve_day03()
    solve_day04()
    solve_day05()
    solve_day06()
    solve_day07()
    solve_day08()
    solve_day09()
    solve_day10()
    solve_day11()
