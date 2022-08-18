"""
Solutions for AOC 2018 Day 3 - "No Matter How You Slice It".
"""

import re
from src.utils.cartography import Location2D


def process_input_file(filepath="./input/day03.txt"):
    """
    Processes the AOC 2018 Day 3 input file into the format required by the
    solver functions. Returns dict mapping claim number to location and size
    """
    with open(filepath, encoding="utf-8") as file:
        regex_claim = re.compile(r"^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$")
        claims = {}
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            if match_claim := regex_claim.match(line):
                claim_id = int(match_claim.group(1))
                loc = Location2D(int(match_claim.group(2)),
                                 int(match_claim.group(3)))
                width = int(match_claim.group(4))
                height = int(match_claim.group(5))
                claims[claim_id] = (loc, width, height)
        return claims


def solve_part1(claims):
    """
    Solves AOC 2018 Day 3 Part 1 // Calculate how many square inches of fabric
    are in two or more claims.
    """
    seen = set()
    overlaps = set()
    for (loc, width, height) in claims.values():
        for delta_y in range(height):
            for delta_x in range(width):
                new_loc = Location2D(loc.x + delta_x, loc.y + delta_y)
                if new_loc in seen:
                    overlaps.add(new_loc)
                else:
                    seen.add(new_loc)
    return len(overlaps)


def solve_part2(claims):
    """
    Solves AOC 2018 Day 3 Part 2 // Determines the ID of the only claim that
    does not overlap.
    """
    # Record which claim IDs occur for each claimed location
    seen = {}
    for (claim_id, (loc, width, height)) in claims.items():
        for delta_y in range(height):
            for delta_x in range(width):
                new_loc = Location2D(loc.x + delta_x, loc.y + delta_y)
                if new_loc not in seen:
                    seen[new_loc] = [claim_id]
                else:
                    seen[new_loc].append(claim_id)
    # Find the IDs of the claims that overlap with another claim
    overlapping_claims = set()
    for claim_ids in (claim_ids for claim_ids in seen.values()
                      if len(claim_ids) > 1):
        overlapping_claims.update(claim_ids)
    # Find the ID of the one claim that does not overlap with another claim
    return (claims.keys() - overlapping_claims).pop()
