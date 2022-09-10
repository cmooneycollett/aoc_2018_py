"""
Solutions for AOC 2018 Day 11.
"""

import itertools


def process_input_file(filepath="./input/day11.txt"):
    """
    Processes the AOC 2018 Day 11 input file into the format required by the
    solver functions. Returns the fuel grid serial number given in the input
    file.
    """
    with open(filepath, encoding="utf-8") as file:
        return int(file.read().strip())


def solve_part1(serial_num):
    """
    Solves AOC 2018 Day 11 Part 1 // Determines the X,Y co-ordinate of the
    top-left fuel cell of the 3x3 square with the largest total power.
    """
    fuel_grid = generate_fuel_grid(serial_num)
    (result_x, result_y, _) = find_square_with_largest_power(fuel_grid, 3)
    return f"{result_x},{result_y}"


def solve_part2(serial_num):
    """
    Solves AOC 2018 Day 11 Part 2 //  Determines the X,Y co-ordinate of the
    top-left fuel cell of the square with the largest total power (size of the
    square is between 1x1 and 300x300).
    """
    result_x = -1
    result_y = -1
    result_side_len = -1
    max_power = None
    fuel_grid = generate_fuel_grid(serial_num)
    for side_len in range(1, 301):
        (x, y, power) = find_square_with_largest_power(fuel_grid, side_len)
        if power < 0:
            break
        if max_power is None or power > max_power:
            max_power = power
            result_x = x
            result_y = y
            result_side_len = side_len
    return f"{result_x},{result_y},{result_side_len}"


def generate_fuel_grid(serial_num):
    """
    Generates a 300x300 fuel grid using the given serial number.
    """
    fuel_grid = []
    for y in range(1, 301):
        row = []
        for x in range(1, 301):
            rack_id = x + 10
            power_level = rack_id * y
            power_level += serial_num
            power_level *= rack_id
            power_level = (power_level % 1000) // 100 - 5
            row.append(power_level)
        fuel_grid.append(row)
    return fuel_grid


def find_square_with_largest_power(fuel_grid, side_len):
    """
    Finds the square (with specified side length) in the fuel grid (300x300)
    with the largest power level. Returns the tuple with the X- and
    Y-coordinates of the top-left cell for the resulting square, and the maximum
    power.
    """
    cells = list(itertools.product(range(300), repeat=2))
    valid_cells = [cell for cell in cells if cell[0] + side_len <= 300 and
                   cell[1] + side_len <= 300]
    deltas = list(itertools.product(range(side_len), repeat=2))
    max_power = None
    result_x = -1
    result_y = -1
    for (x, y) in valid_cells:
        power_total = 0
        for (delta_x, delta_y) in deltas:
            power_total += fuel_grid[y + delta_y][x + delta_x]
        if max_power is None or power_total > max_power:
            max_power = power_total
            result_x = x + 1
            result_y = y + 1
    return (result_x, result_y, max_power)
