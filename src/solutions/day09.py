"""
Solutions for AOC 2018 Day 9.
"""

from collections import deque
import re


def process_input_file(filepath="./input/day09.txt"):
    """
    Processes the AOC 2018 Day 9 input file into the format required by the
    solver functions. Returns a tuple containing the number of players and the
    number of points for the last marble in the marble game.
    """
    with open(filepath, encoding="utf-8") as file:
        regex_input = re.compile(
            r"^(\d+) players; last marble is worth (\d+) points$")
        if match_input := regex_input.match(file.read().strip()):
            num_players = int(match_input.group(1))
            num_points_last_marble = int(match_input.group(2))
            return (num_players, num_points_last_marble)
        raise RuntimeError("D9: invalid input file format!")


def solve_part1(input_data):
    """
    Solves AOC 2018 Day 9 Part 1 // Determines the winning score for the elf in
    the marble game, using the number of players and last marble score given in
    the input data.
    """
    (num_players, num_points_last_marble) = input_data
    return play_marble_game(num_players, num_points_last_marble)


def solve_part2(input_data):
    """
    Solves AOC 2018 Day 9 Part 2 // Determines the winning score for the elf in
    the marble game, using the number of players and 100 times the last marble
    score given in the input data
    """
    (num_players, num_points_last_marble) = input_data
    return play_marble_game(num_players, num_points_last_marble * 100)


def play_marble_game(num_players, num_points_last_marble):
    """
    Plays the marble game with the given number of players and points for the
    last marble. Returns the number of points gained by the winning elf.
    """
    marbles = deque([0])
    scores = {}
    for marble in range(1, num_points_last_marble + 1):
        # Determine the current elf
        elf = marble % num_players
        if marble % 23 == 0:
            marbles.rotate(7)
            if elf not in scores:
                scores[elf] = 0
            scores[elf] += marbles.pop() + marble
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(marble)
    return max(scores.values(), default=0)
