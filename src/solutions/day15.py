"""
Solutions for AOC 2018 Day 15.
"""

from enum import Enum, auto, unique

@unique
class TileType(Enum):
    """
    Represents the different types of types existing in the tile map.
    """
    WALL = auto()
    SPACE = auto()


def process_input_file(filepath="./input/day15.txt"):
    """
    Processes the AOC 2018 Day 15 input file into the format required by the
    solver functions. Returns a tuple containing map of grid tiles, starting
    locations of elves, and starting locations of goblins.
    """
    with open(filepath, encoding="utf-8") as file:
        tile_map = {}
        elf_locations = []
        goblin_locations = []
        y = 0
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            x = 0
            for char in line:
                match char:
                    case "#":
                        tile_map[(x, y)] = TileType.WALL
                    case ".":
                        tile_map[(x, y)] = TileType.SPACE
                    case "G":
                        tile_map[(x, y)] = TileType.SPACE
                        goblin_locations.append((x, y))
                    case "E":
                        tile_map[(x, y)] = TileType.SPACE
                        elf_locations.append((x, y))
                    case _:
                        raise RuntimeError(f"Day 15: unexpected char in input file: {char}")
                x += 1
            y += 1
        return (tile_map, elf_locations, goblin_locations)



def solve_part1(input_data):
    """
    Solves AOC 2018 Day 15 Part 1 // Determines the outcome value of the combat
    between elves and goblins (product of number of full rounds conducted and
    the sum of the hit points of all remaining units at the moment combat ends).
    """
    (tile_map, start_elf_locs, start_goblin_locs) = input_data
    return ()


def solve_part2(_input_data):
    """
    Solves AOC 2018 Day 15 Part 2 // ###
    """
    return NotImplemented
