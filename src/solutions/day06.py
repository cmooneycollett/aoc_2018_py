"""
Solutions for AOC 2018 Day 6 - "Chronal Coordinates".
"""

from dataclasses import dataclass
from typing import List
from src.utils.cartography import Location2D


@dataclass
class MinMax:
    """
    Stores the minimum and maximum x- and y-coordinate values for a collection
    of 2D locations.
    """
    x_min: int
    x_max: int
    y_min: int
    y_max: int


def process_input_file(filepath="./input/day06.txt"):
    """
    Processes the AOC 2018 Day 6 input file into the format required by the
    solver functions. Returns list of Location2D objects with the x- and
    y-coordinates listed in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        points = []
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            coords = [int(val) for val in line.split(", ")]
            points.append(Location2D(coords[0], coords[1]))
        return points


def solve_part1(points: List[Location2D]):
    """
    Solves AOC 2018 Day 6 Part 1 // Calculates the largest area close to a
    single point that is not infinite.
    """
    # Calculate minimum and maximum x- and y-coordinates
    minmax = calculate_minmax(points)
    # Check each point
    region_map = {}
    boundary_points = set()
    area_counts = {point_id: 0 for point_id in range(len(points))}
    for y in range(minmax.y_min, minmax.y_max + 1):
        for x in range(minmax.x_min, minmax.x_max + 1):
            min_dist = None
            closest_point_ids = []
            loc = Location2D(x, y)
            if x == minmax.x_min or x == minmax.x_max or y == minmax.y_min or \
                    y == minmax.y_max:
                boundary_points.add(loc)
            for (point_id, point) in enumerate(points):
                dist = abs(x - point.x) + abs(y - point.y)
                if min_dist is None or dist < min_dist:
                    closest_point_ids = [point_id]
                    min_dist = dist
                elif dist == min_dist:
                    closest_point_ids.append(point_id)
            # Only update area count if the location is not shared
            region_map[loc] = closest_point_ids
            if len(closest_point_ids) == 1:
                area_counts[closest_point_ids[0]] += 1
    # Exclude regions with presence on boundary
    for point in boundary_points:
        for point_id in region_map[point]:
            if point_id in area_counts:
                del area_counts[point_id]
    return max(area_counts.values())


def solve_part2(points: List[Location2D]):
    """
    Solves AOC 2018 Day 6 Part 2 // Calculates the size of the region containing
    all locations which have a total distance to all other locations of less
    than 10000.
    """
    cap = 10000
    buffer = cap // (2 * len(points)) + 1
    minmax = calculate_minmax(points)
    safe_points = 0
    for y in range(minmax.y_min - buffer, minmax.y_max + buffer + 1):
        for x in range(minmax.x_min - buffer, minmax.x_max + buffer + 1):
            total_manhattan_dist = 0
            for point in points:
                total_manhattan_dist += abs(x - point.x) + abs(y - point.y)
            if total_manhattan_dist < cap:
                safe_points += 1
    return safe_points


def get_valid_next_states(point_id, loc, seen, minmax):
    """
    Gets the valid next states for the breadth-first search in the coordinates
    grid.
    """
    for (delta_x, delta_y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_loc = Location2D(loc.x + delta_x, loc.y + delta_y)
        if minmax.x_min > new_loc.x > minmax.x_max and \
                minmax.y_min > new_loc.y > minmax.y_max:
            continue
        if new_loc in seen and point_id in seen[new_loc]:
            continue
        yield (point_id, new_loc, loc)


def calculate_minmax(points):
    """
    Calculates the minimum and maximum x- and y-coordinates for the given 2D
    points. Returns a MinMax object with the resulting values.
    """
    x_min = min(point.x for point in points)
    x_max = max(point.x for point in points)
    y_min = min(point.y for point in points)
    y_max = max(point.y for point in points)
    return MinMax(x_min, x_max, y_min, y_max)
