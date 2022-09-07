"""
Solutions for AOC 2018 Day 10.
"""

from copy import deepcopy
import re


class LightPoint:
    """
    Represents a two-dimensional light point with position and velocity (integer
    values)
    """

    def __init__(self, pos_x, pos_y, vel_x, vel_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def move(self):
        """
        Updates the position of the point by applying its velocity.
        """
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y


def process_input_file(filepath="./input/day10.txt"):
    """
    Processes the AOC 2018 Day 10 input file into the format required by the
    solver functions. Returns list of light point objects specified by positions
    and velocities in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        points = []
        regex_line = re.compile(
            r"^position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>$")
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            if match_line := regex_line.match(line):
                pos_x = int(match_line.group(1))
                pos_y = int(match_line.group(2))
                vel_x = int(match_line.group(3))
                vel_y = int(match_line.group(4))
                points.append(LightPoint(pos_x, pos_y, vel_x, vel_y))
        return points


def solve_part1(input_points):
    """
    Solves AOC 2018 Day 10 Part 1 // Determines the string representation of the
    message appears from an arrangement of the input light points.
    """
    (message, _) = simulate_points(input_points)
    return message


def solve_part2(input_points):
    """
    Solves AOC 2018 Day 10 Part 2 // Determines the number of steps taken until
    the input light points display their message.
    """
    (_, steps) = simulate_points(input_points)
    return steps


def simulate_points(input_points):
    """
    Runs a simulation of the input points until the area of the bounding box is
    less than 1000. Returns the string representation of the message displayed
    by the points and the number of steps taken.
    """
    points = [deepcopy(point) for point in input_points]
    (min_x, max_x, min_y, max_y) = (0, 0, 0, 0)
    steps = 0
    while True:
        # Check bounding box area
        min_x = min(point.pos_x for point in points)
        max_x = max(point.pos_x for point in points)
        min_y = min(point.pos_y for point in points)
        max_y = max(point.pos_y for point in points)
        box_area = (max_x - min_x + 1) * (max_y - min_y + 1)
        if box_area <= 1000:
            break
        # Move points
        for point in points:
            point.move()
        steps += 1
    # Generate location map
    message_raw = generate_raw_message(points, min_x, max_x, min_y, max_y)
    message = parse_raw_message(message_raw)
    return (message, steps)


def generate_raw_message(points, min_x, max_x, min_y, max_y):
    """
    Generates the raw message array from a list of light points.
    """
    # Extract locations of all points
    point_locs = set()
    for point in points:
        point_locs.add((point.pos_x, point.pos_y))
    # Build up raw message by checking light point presence within bounding box
    message_raw = []
    for y in range(min_y, max_y + 1):
        message_raw_row = []
        for x in range(min_x, max_x + 1):
            if (x, y) in point_locs:
                message_raw_row.append("#")
            else:
                message_raw_row.append(".")
        message_raw.append(message_raw_row)
    return message_raw


def parse_raw_message(raw_message):
    """
    Parses the raw message array. Returns the string representation of the
    message.
    """
    letters = {
        "..##...#..#.#....##....##....########....##....##....##....#": "A",
        "#####.#....##....##....######.#....##....##....##....######.": "B",
        ".######.....#.....#.....#.....#.....#.....#.....#......#####": "C",
        "####..#...#.#....##....##....##....##....##....##...#.####..": "D",
        "#######.....#.....#.....#####.#.....#.....#.....#.....######": "E",
        "#######.....#.....#.....#####.#.....#.....#.....#.....#.....": "F",
        ".####.#....##.....#.....#.....#..####....##....##...##.###.#": "G",
        "#....##....##....##....########....##....##....##....##....#": "H",
        "######..#.....#.....#.....#.....#.....#.....#.....#...######": "I",
        "######...#.....#.....#.....#.....#.....#..#..#..#..#...##...": "J",
        "#....##...#.#..#..#.#...##....##....#.#...#..#..#...#.#....#": "K",
        "#.....#.....#.....#.....#.....#.....#.....#.....#.....######": "L",
        ".#..#..####.#.##.##.##.##....##....##....##....##....##....#": "M",
        "#....##....###...##.#..##..#.##...###....##....##....##....#": "N",
        ".####.#....##....##....##....##....##....##....##....#.####.": "O",
        "####..#...#.#....##....##...#.####..#.....#.....#.....#.....": "P",
        "#####.#...#.#...#.#...#.#...#.#.#.#.#..##.#####......#.....#": "Q",
        "#####.#....##....##....######.##....#.#...#..#..#...#.#....#": "R",
        ".######.....#.....#......####......#.....#.....#.....######.": "S",
        "######..#.....#.....#.....#.....#.....#.....#.....#.....#...": "T",
        "#....##....##....##....##....##....##....##....##....#.####.": "U",
        "#....##....##....##....##....##....##....##....#.#..#...##..": "V",
        "#....##....##....##....##.##.##.##.##.##.##.##.#.#..#..#..#.": "W",
        "#....##....#.#..#..#..#...##....##...#..#..#..#.#....##....#": "X",
        "#....##....##....#.#..#...##....##....##....##....##....##..": "Y",
        "######.....#.....#....#....#....#....#....#.....#.....######": "Z",
    }
    message = []
    for x_start in range(0, len(raw_message[0]), 8):
        letter_chunk = ""
        for row in raw_message:
            for x in range(x_start, x_start + 6):
                letter_chunk += row[x]
        # Check which letter the current chunk represents
        if letter_chunk in letters:
            message.append(letters[letter_chunk])
        else:
            message.append("#")
    return "".join(message)
